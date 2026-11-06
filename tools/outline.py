"""Turns live <text> in an SVG into filled paths using the site's fonts, then writes a dark and a light copy.
GitHub shows README images without web fonts, so every letter has to be a shape.
usage: python outline.py <raw_dir> <out_dir>   (or import outline_svg / themed)"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
FONTS = Path(__file__).parent / 'fonts'
_cache = {}

THEMES = {
    'dark': {'gv': '#0E0E0E', 'gi': '#EDEDED', 'gm': '#A0A0A0', 'ga': '#FF4A3D', 'gc': '#161616', 'gl': '#2A2A2A'},
    'light': {'gv': '#F2EFE9', 'gi': '#111111', 'gm': '#555250', 'ga': '#D7261E', 'gc': '#FAF8F4', 'gl': '#DAD5CC'},
}


def font_for(family, weight):
    fam = (family or '').lower()
    w = int(weight or 400)
    if 'bricolage' in fam:
        name = 'bricolage-800' if w >= 800 else 'bricolage-700'
    elif 'caveat' in fam:
        name = 'caveat-latin-600-normal'
    elif 'plex' in fam or 'mono' in fam:
        name = 'ibm-plex-mono-latin-400-normal'
    else:
        name = 'geist-600' if w >= 600 else 'geist-400'
    if name not in _cache:
        f = TTFont(FONTS / f'{name}.woff2')
        _cache[name] = (f, f.getGlyphSet(), f.getBestCmap(), f['hmtx'], f['head'].unitsPerEm)
    return _cache[name]


def run_width(s, attrs):
    f, gs, cmap, hmtx, upm = font_for(attrs.get('font-family'), attrs.get('font-weight'))
    size, ls = float(attrs.get('font-size', 16)), float(attrs.get('letter-spacing', 0))
    return sum(hmtx[cmap.get(ord(c), '.notdef')][0] * size / upm + ls for c in s)


def draw(s, x, y, attrs, pen_out):
    f, gs, cmap, hmtx, upm = font_for(attrs.get('font-family'), attrs.get('font-weight'))
    size, ls = float(attrs.get('font-size', 16)), float(attrs.get('letter-spacing', 0))
    k = size / upm
    for c in s:
        g = cmap.get(ord(c), '.notdef')
        if c != ' ':
            gs[g].draw(TransformPen(pen_out, (k, 0, 0, -k, x, y)))
        x += hmtx[g][0] * k + ls
    return x


INHERIT = ('font-family', 'font-size', 'font-weight', 'letter-spacing', 'text-anchor', 'fill')


def runs_of(text_el, inh):
    """[(string, x|None, y|None, attrs)] in document order."""
    base = dict(inh)
    base.update({k: v for k, v in text_el.attrib.items() if k in INHERIT})
    out = []
    if text_el.text and text_el.text.strip('\n'):
        out.append((text_el.text, text_el.get('x'), text_el.get('y'), base))
    for ts in text_el:
        a = dict(base)
        a.update({k: v for k, v in ts.attrib.items() if k in INHERIT})
        if ts.text:
            out.append((ts.text, ts.get('x'), ts.get('y'), a))
        for inner in ts:  # one level of nesting, e.g. a coloured prompt inside a line
            ia = dict(a)
            ia.update({k: v for k, v in inner.attrib.items() if k in INHERIT})
            if inner.text:
                out.append((inner.text, None, None, ia))
            if inner.tail and inner.tail.strip('\n'):
                out.append((inner.tail, None, None, a))
        if ts.tail and ts.tail.strip('\n'):
            out.append((ts.tail, None, None, base))
    return out


def outline_text(text_el, inh, after=None):
    runs = runs_of(text_el, inh)
    x = float(text_el.get('x', 0))
    y = float(text_el.get('y', 0))
    if after is not None:
        x = after
    anchor = (dict(inh) | text_el.attrib).get('text-anchor', 'start')
    if anchor != 'start':
        w = sum(run_width(s, a) for s, _, _, a in runs)
        x -= w if anchor == 'end' else w / 2
    g = ET.Element(f'{{{NS}}}g')
    for k in ('class', 'style', 'opacity', 'transform'):
        if text_el.get(k):
            g.set(k, text_el.get(k))
    start_x = x
    for s, rx, ry, a in runs:
        if rx is not None:
            x = float(rx)
        if ry is not None:
            y = float(ry)
        pen = SVGPathPen(font_for(a.get("font-family"), a.get("font-weight"))[1], ntos=lambda v: ("%.1f" % v).rstrip("0").rstrip("."))
        x = draw(s, x, y, a, pen)
        d = pen.getCommands()
        if d:
            p = ET.SubElement(g, f'{{{NS}}}path')
            p.set('d', d)
            p.set('fill', a.get('fill', '#000'))
    return g, x, start_x


def outline_svg(src):
    root = ET.fromstring(src)
    k2_end = None

    def walk(node, inh):
        nonlocal k2_end
        for i, ch in enumerate(list(node)):
            tag = ch.tag.split('}')[-1]
            if tag == 'text':
                cls = ch.get('class', '')
                after = k2_end + 2 if ('kd' in cls.split() and k2_end is not None) else None
                g, end_x, _ = outline_text(ch, inh, after)
                if 'k2' in cls.split():
                    k2_end = end_x
                node.remove(ch)
                node.insert(i, g)
            elif tag in ('g', 'svg', 'a'):
                walk(ch, inh | {k: v for k, v in ch.attrib.items() if k in INHERIT})
            elif tag == 'style':
                continue

    walk(root, {})
    for el in root.iter():  # font attributes are meaningless once text is gone
        for k in ('font-family', 'font-size', 'font-weight', 'letter-spacing', 'text-anchor'):
            el.attrib.pop(k, None)
    return ET.tostring(root, encoding='unicode')


def themed(svg, theme):
    t = THEMES[theme]
    return re.sub(r'var\(--g([vimacl])\)', lambda m: t['g' + m.group(1)], svg)


if __name__ == '__main__':
    raw, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    for f in sorted(raw.glob('*.svg')):
        flat = outline_svg(f.read_text())
        assert '<text' not in flat, f
        for th in THEMES:
            (out / f'{f.stem}-{th}.svg').write_text(themed(flat, th))
    print('wrote', len(list(out.glob('*.svg'))), 'files')
