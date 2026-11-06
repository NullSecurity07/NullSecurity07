"""Draws 'Offscan scans your year' from the real GitHub contribution calendar.
Writes assets/scan-dark.svg and assets/scan-light.svg. Run daily by .github/workflows/scan.yml.
usage: GITHUB_TOKEN=... python tools/scan.py [login]"""
import datetime as dt
import json
import os
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from outline import THEMES, outline_svg, themed  # noqa: E402

LOGIN = sys.argv[1] if len(sys.argv) > 1 else 'NullSecurity07'
ROOT = Path(__file__).resolve().parent.parent
LEVEL = {'NONE': 0, 'FIRST_QUARTILE': 1, 'SECOND_QUARTILE': 2, 'THIRD_QUARTILE': 3, 'FOURTH_QUARTILE': 4}
LV = [0.08, 0.3, 0.5, 0.75, 1]
QUERY = """query($login:String!,$from:DateTime!,$to:DateTime!){user(login:$login){contributionsCollection(from:$from,to:$to){
contributionCalendar{totalContributions weeks{contributionDays{contributionLevel weekday}}}}}}"""


def fetch(year):
    token = os.environ['GITHUB_TOKEN']
    now = dt.datetime.now(dt.timezone.utc)
    body = json.dumps({'query': QUERY, 'variables': {'login': LOGIN, 'from': f'{year}-01-01T00:00:00Z', 'to': now.strftime('%Y-%m-%dT%H:%M:%SZ')}}).encode()
    req = urllib.request.Request('https://api.github.com/graphql', body, {'Authorization': f'bearer {token}', 'User-Agent': 'profile-scan'})
    data = json.load(urllib.request.urlopen(req, timeout=30))
    if 'errors' in data:
        raise SystemExit(data['errors'])
    c = data['data']['user']['contributionsCollection']
    weeks = [[None] * 7 for _ in c['contributionCalendar']['weeks']]
    for w, week in zip(weeks, c['contributionCalendar']['weeks']):
        for d in week['contributionDays']:
            w[d['weekday']] = LEVEL[d['contributionLevel']]
    return weeks, c["contributionCalendar"]["totalContributions"]


def draw(weeks, commits, year):
    n = len(weeks)
    pitch = min(26, 1160 / n)  # a full year (53 weeks) still fits the 1280 frame
    size = round(pitch * 0.77, 1)
    d = 9
    w = n * pitch
    cells = []
    for c, col in enumerate(weeks):
        for r, v in enumerate(col):
            if v is None:  # days after today, or before Jan 1
                continue
            anim = f' class="oc" style="--o:{LV[v]};animation-delay:{c / n * d * 0.85:.2f}s"' if v else ''
            cells.append(f'<rect x="{60 + c * pitch:.1f}" y="{80 + r * 26}" width="{size}" height="20" rx="4" fill="var(--gm)" fill-opacity="{LV[v]}"{anim}/>')
    mono = 'font-family="IBM Plex Mono, monospace"'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 330" role="img" aria-label="Offscan scans {year}: {commits:,} contributions, all on this machine">
<style>
.os{{animation:os {d}s linear infinite}}@keyframes os{{0%{{transform:translateX(0)}}85%,100%{{transform:translateX({w:.0f}px)}}}}
.oc{{animation:oc {d}s linear infinite}}@keyframes oc{{0%{{fill:var(--gm);fill-opacity:var(--o)}}2%{{fill:#fff;fill-opacity:1}}5%,95%{{fill:var(--ga);fill-opacity:var(--o)}}100%{{fill:var(--gm);fill-opacity:var(--o)}}}}
.ol{{opacity:0;animation:ol {d}s linear infinite}}@keyframes ol{{0%,84%{{opacity:0}}87%,98%{{opacity:1}}100%{{opacity:0}}}}
@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .ol {{ opacity: 1; }} }}
</style>
<rect width="1280" height="330" rx="10" fill="var(--gv)"/>
<text x="60" y="48" {mono} font-size="19" fill="var(--gi)"><tspan fill="var(--ga)">$ </tspan>offscan scan ~/{year} --local</text>
{''.join(cells)}
<g class="os"><rect x="52" y="70" width="4" height="196" fill="var(--ga)"/><rect x="40" y="70" width="12" height="196" fill="var(--ga)" opacity=".18"/></g>
<text class="ol" x="60" y="300" {mono} font-size="18" fill="var(--gi)">{commits:,} contributions scanned. <tspan fill="var(--ga)">0 lines of code left this machine.</tspan></text>
</svg>'''


if __name__ == '__main__':
    year = dt.date.today().year
    weeks, commits = fetch(year)
    flat = outline_svg(draw(weeks, commits, year))
    out = ROOT / 'assets'
    out.mkdir(exist_ok=True)
    for th in THEMES:
        (out / f'scan-{th}.svg').write_text(themed(flat, th))
    print(f'{LOGIN} {year}: {len(weeks)} weeks, {commits} contributions')
