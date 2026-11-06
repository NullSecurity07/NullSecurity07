// Pulls the static README images out of the design page's generators (the same code the preview used),
// so the files match the approved draft exactly. Writes raw SVGs with live text; outline.py turns text into shapes.
// usage: node extract.mjs <template.html> <imgs.json> <outdir>
import fs from 'node:fs';
const [tpl, imgs, out] = process.argv.slice(2);
const html = fs.readFileSync(tpl, 'utf8');
const src = html.slice(html.lastIndexOf('<script>') + 8, html.lastIndexOf('</script>')).replace('__IMGS__', fs.readFileSync(imgs, 'utf8'));
const el = () => ({ innerHTML: '', classList: { toggle() {} }, querySelectorAll: () => [], querySelector: () => null, addEventListener() {} });
globalThis.document = { addEventListener() {}, getElementById: el, querySelector: () => null, querySelectorAll: () => [] };
globalThis.localStorage = { getItem: () => null, setItem() {} };
const fn = new Function(src + `
return {
  header: ink(),
  now: nowNumbers(),
  footer: lock(),
  cards: PROJ.map((p, i) => [p[0], card(p, 'r' + i)]),
  links: LINKS2.map((l) => [l[0], linkImg(l)]),
};`);
const r = fn();
fs.mkdirSync(out, { recursive: true });
const svg = (s) => s.replace(/^\s*<svg /, '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" ').replace(/ style="height:46px;width:auto"/, '');
fs.writeFileSync(`${out}/header.svg`, svg(r.header));
fs.writeFileSync(`${out}/now.svg`, svg(r.now));
fs.writeFileSync(`${out}/footer.svg`, svg(r.footer));
for (const [slug, s] of r.cards) fs.writeFileSync(`${out}/case-${slug}.svg`, svg(s));
for (const [k, s] of r.links) fs.writeFileSync(`${out}/link-${k}.svg`, svg(s));
console.log('raw svgs:', fs.readdirSync(out).length);
