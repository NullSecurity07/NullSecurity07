"""Writes README.md from the asset list. usage: python tools/readme.py"""
from pathlib import Path

SITE = 'https://adithyapoojary.is-a.dev'


def pic(stem, alt, width=None, height=None):
    size = f' width="{width}"' if width else f' height="{height}"' if height else ' width="100%"'
    return (f'<picture><source media="(prefers-color-scheme: light)" srcset="assets/{stem}-light.svg">'
            f'<img src="assets/{stem}-dark.svg" alt="{alt}"{size}></picture>')


LINKS = [('site', 'Site: adithyapoojary.is-a.dev', SITE), ('linkedin', 'LinkedIn: in/adithyapoojary', 'https://www.linkedin.com/in/adithyapoojary/'),
         ('tryhackme', 'TryHackMe: nullsec0001', 'https://tryhackme.com/p/nullsec0001'), ('email', 'Email: thisisadithya07@gmail.com', 'mailto:thisisadithya07@gmail.com')]
CASES = [('offscan', 'Offscan: finds security bugs in your code with AI that runs on your own machine'),
         ('jarvis', 'Jarvis: move notes, 3D models and live windows with your bare hands over a webcam'),
         ('cubicle', 'Cubicle: a canvas where a founder works with a workforce of AI agents and keeps every decision'),
         ('caliber', "Caliber: BLC's coding and assessment platform, designed and built as lead engineer"),
         ('hackypi', 'HackyPi: a USB test device for authorized penetration tests that ships disarmed'),
         ('deauthreaper', 'Deauth Reaper: a character-driven pwnagotchi for authorized Wi-Fi security practice')]

links = '&nbsp;&nbsp;&nbsp;'.join(f'<a href="{u}">{pic("link-" + k, a, height=46)}</a>' for k, a, u in LINKS)
cards = '\n'.join(f'<a href="{SITE}/work/{s}/">{pic("case-" + s, a, width="49%")}</a>' for s, a in CASES)

readme = f'''<!-- 61646974687961706f6f6a6172792e69732d612e6465762f3132 -->
<a href="{SITE}">{pic('header', 'Adithya Poojary. Founder of ThreatScope, maker of Offscan. 19-year-old founder building secure AI products, solo.')}</a>

<p>{links}</p>

{pic('now', 'Right now: building Offscan and taking it to developers; leading platform and security engineering at BLC; 3rd-year engineering student in AI and ML. 5,000+ students use the platform I built at BLC, 4,600+ automated tests in Offscan, 5,000+ commits in 2026 across three products, top 6% worldwide on TryHackMe.')}

<p>
{cards}
</p>

{pic('scan', 'Offscan scans this year of contributions, locally. Redrawn every day.')}

### Capture the flag

One flag is hidden in this profile. It looks like `flag{{...}}`. Found it? [Submit it as an issue](https://github.com/NullSecurity07/NullSecurity07/issues/new?title=flag:%20) with the title `flag: <your flag>` and the bot checks it in under a minute.

```
clue 1: the source remembers what the page forgets
```

<!-- hof:start -->
| # | Solver | Solved |
|---|---|---|
| No solvers yet. Be the first. | | |
<!-- hof:end -->

<details><summary>sudo</summary>

```
[sudo] password for visitor: ********
access granted.

you read past the cards. most people don't.
I am always up for talking security, AI, or building
something hard. thisisadithya07@gmail.com
```

</details>

<a href="mailto:thisisadithya07@gmail.com">{pic('footer', 'Target acquired. You found Adithya. Say hi: thisisadithya07@gmail.com')}</a>
'''
Path(__file__).resolve().parent.parent.joinpath('README.md').write_text(readme)
print('README.md', len(readme), 'chars')
