"""Adds a solver to the hall of fame table in the README, between the hof markers. Ignores repeat solvers.
usage: python halloffame.py README.md <login> <YYYY-MM-DD>"""
import re
import sys
from pathlib import Path

path, login, day = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
if not re.fullmatch(r'[A-Za-z0-9-]{1,39}', login):  # GitHub login rules; keeps markdown injection out
    sys.exit('bad login')
text = path.read_text()
m = re.search(r'(<!-- hof:start -->\n)(.*?)(<!-- hof:end -->)', text, re.S)
rows = [r for r in m.group(2).splitlines() if r.startswith('| ') and not r.startswith('| #') and not r.startswith('| No solvers')]
if any(f'[@{login}]' in r for r in rows):
    sys.exit(0)
rows.append(f'| {len(rows) + 1} | [@{login}](https://github.com/{login}) | {day} |')
table = '| # | Solver | Solved |\n|---|---|---|\n' + '\n'.join(rows) + '\n'
path.write_text(text[:m.start(2)] + table + text[m.end(2):])
