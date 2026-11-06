"""Fills a README draft (from repos/<name>/README.md + meta.json) with the banner, badges and preview, inside a repo checkout.
Images go to <checkout>/.github/readme/. usage: python finalize.py <name> <drafts_dir> <checkout> [preview_file]"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).parent
name, drafts, checkout = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
preview_file = Path(sys.argv[4]) if len(sys.argv) > 4 else None
meta = json.loads((drafts / 'meta.json').read_text())
img = checkout / '.github' / 'readme'
img.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, '-I', str(TOOLS / 'banner.py'), name, str(drafts / 'meta.json'), str(img)], check=True)


def pic(stem, alt, style):
    return (f'<picture><source media="(prefers-color-scheme: light)" srcset=".github/readme/{stem}-light.svg">'
            f'<img src=".github/readme/{stem}-dark.svg" alt="{alt}" {style}></picture>')


home = meta.get('homepage') or 'https://adithyapoojary.is-a.dev'
banner = f'<p align="center"><a href="{home}">{pic("banner", meta.get("title", name) + ": " + meta["pitch"], "width=\"100%\"")}</a></p>'
badges = f'<p align="center">{pic("badges", ", ".join(f"{a}: {b}" for a, b in meta.get("badges", [])), "height=\"30\"")}</p>'
preview = ''
if preview_file:
    shutil.copy(preview_file, img / ('preview' + preview_file.suffix))
    preview = (f'<p align="center"><a href="{home}"><img src=".github/readme/preview{preview_file.suffix}" width="100%" '
               f'alt="{meta.get("title", name)} in use"></a><br><sub>A clip from the walkthrough. <a href="{home}">Watch the full video</a>.</sub></p>')
elif meta.get('preview', 'none').startswith('image:'):
    p = meta['preview'].split(':', 1)[1].lstrip('/')
    preview = f'<p align="center"><img src="{p}" width="100%" alt="{meta.get("title", name)} screenshot"></p>'

text = (drafts / 'README.md').read_text()
text = re.sub(r'^<!-- banner:.*?-->\n', '', text, flags=re.M)
text = re.sub(r'^<p align="center"><picture>…banner…</picture></p>\n?', '', text, flags=re.M)
text = re.sub(r'^(?:<p align="center">)?BADGES(?:</p>)?[ \t]*$', badges, text, count=1, flags=re.M)
text = re.sub(r'^PREVIEW[ \t]*$', preview, text, count=1, flags=re.M)
text = banner + '\n' + text.lstrip()
assert 'BADGES' not in text and '\nPREVIEW' not in text and '—' not in text, 'placeholder or em dash left'
(checkout / 'README.md').write_text(text)
print(name, 'README filled,', len(text), 'chars')
