"""Draws a repo's README banner and badge row in the profile's riso style, from its meta.json.
Writes <out>/banner-{dark,light}.svg and <out>/badges-{dark,light}.svg. All still images (one moving thing per screen).
usage: python banner.py <repo_name> <meta.json> <out_dir>"""
import json
import math
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).parent))
from outline import THEMES, outline_svg, run_width, themed  # noqa: E402

DISP = 'Bricolage Grotesque'
BODY = 'Geist'
MONO = 'IBM Plex Mono'


def fit(text, family, weight, size, max_w, ls=0.0):
    while size > 28 and run_width(text, {'font-family': family, 'font-weight': weight, 'font-size': size, 'letter-spacing': ls * size / 96}) > max_w:
        size -= 2
    return size


def banner(repo, meta):
    title = meta.get('title') or repo.replace('-', ' ')
    pitch = meta['pitch']
    size = fit(title, DISP, 800, 104, 700, -2.5)
    ls = -2.5 * size / 96
    tw = run_width(title, {'font-family': DISP, 'font-weight': 800, 'font-size': size, 'letter-spacing': ls})
    base = 190
    dots = []
    for i, x in enumerate(range(800, 1260, 20)):  # halftone field, denser and bigger toward the right edge
        for j, y in enumerate(range(26, 306, 20)):
            t = (x - 800) / 460
            wave = 0.5 + 0.5 * math.sin(j * 0.55 + i * 0.35)
            r = 0.8 + 6.2 * t * (0.55 + 0.45 * wave)
            if r > 1.1:
                dots.append(f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="var(--ga)" fill-opacity="{0.25 + 0.55 * t:.2f}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 320" role="img" aria-label="{escape(title)}: {escape(pitch)}">
<rect width="1280" height="320" rx="10" fill="var(--gv)"/>
{''.join(dots)}
<text x="64" y="66" font-family="{MONO}" font-size="15" letter-spacing="1.5" fill="var(--gm)">NULLSECURITY07 / {escape(repo.upper())}</text>
<text x="60" y="{base}" font-family="{DISP}" font-weight="800" font-size="{size}" letter-spacing="{ls:.2f}" fill="var(--gi)">{escape(title)}</text>
<circle cx="{60 + tw + size * 0.16:.1f}" cy="{base - size * 0.07:.1f}" r="{size * 0.085:.1f}" fill="var(--ga)"/>
<text x="64" y="{base + 50}" font-family="{BODY}" font-size="26" fill="var(--gm)">{escape(pitch)}</text>
<text x="64" y="284" font-family="{MONO}" font-size="14" fill="var(--gm)">by Adithya Poojary · adithyapoojary.is-a.dev</text>
</svg>'''


def badges(meta):
    x, parts = 0.0, []
    for label, value in meta.get('badges', [])[:5]:
        lw = run_width(label.upper(), {'font-family': MONO, 'font-size': 12, 'letter-spacing': 1})
        vw = run_width(value, {'font-family': BODY, 'font-weight': 600, 'font-size': 15})
        w = 14 + lw + 10 + vw + 14
        parts.append(f'<g transform="translate({x:.1f} 0)"><rect x=".5" y=".5" width="{w:.1f}" height="33" rx="5" fill="var(--gc)" stroke="var(--gl)"/>'
                     f'<rect x=".5" y="8" width="2.5" height="18" fill="var(--ga)"/>'
                     f'<text x="14" y="21.5" font-family="{MONO}" font-size="12" letter-spacing="1" fill="var(--gm)">{escape(label.upper())}</text>'
                     f'<text x="{14 + lw + 10:.1f}" y="22" font-family="{BODY}" font-weight="600" font-size="15" fill="var(--gi)">{escape(value)}</text></g>')
        x += w + 10
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x - 10 + 1:.0f} 34" role="img" aria-label="{escape(", ".join(f"{a}: {b}" for a, b in meta.get("badges", [])))}">{"".join(parts)}</svg>', x - 10 + 1


if __name__ == '__main__':
    repo, meta_path, out = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    meta = json.loads(meta_path.read_text())
    out.mkdir(parents=True, exist_ok=True)
    b = outline_svg(banner(repo, meta))
    g, gw = badges(meta)
    g = outline_svg(g)
    for th in THEMES:
        (out / f'banner-{th}.svg').write_text(themed(b, th))
        (out / f'badges-{th}.svg').write_text(themed(g, th))
    print(repo, 'banner + badges written, badge row width', round(gw))
