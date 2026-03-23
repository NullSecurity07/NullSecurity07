<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0e17,50:0d1b2a,100:00b4d8&height=220&section=header&text=Adithya%20Poojary&fontSize=52&fontColor=ffffff&fontAlignY=38&fontAlign=50&desc=Security%20Researcher%20%C2%B7%20AI%20Engineer%20%C2%B7%20Founder&descSize=16&descAlignY=58&descAlign=50&descColor=90e0ef&animation=fadeIn" width="100%"/>

</div>

<br/>

<div align="center">

<a href="https://www.linkedin.com/in/adithyapoojary/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0d1b2a?style=for-the-badge&logo=linkedin&logoColor=00b4d8"/>
</a>
&nbsp;
<a href="https://tryhackme.com/p/nullsec0001" target="_blank">
  <img src="https://img.shields.io/badge/TryHackMe-0d1b2a?style=for-the-badge&logo=tryhackme&logoColor=00b4d8"/>
</a>
&nbsp;
<a href="mailto:nullsec0001@proton.me">
  <img src="https://img.shields.io/badge/nullsec0001@proton.me-0d1b2a?style=for-the-badge&logo=protonmail&logoColor=00b4d8"/>
</a>
&nbsp;
<a href="mailto:thisisadithya07@gmail.com">
  <img src="https://img.shields.io/badge/thisisadithya07@gmail.com-0d1b2a?style=for-the-badge&logo=gmail&logoColor=00b4d8"/>
</a>

</div>

<br/><br/>

---

<br/>

<div align="center">

### — Who I Am —

</div>

<br/>

<img src="https://media.giphy.com/media/RbDKaczqWovIugyJmW/giphy.gif" width="180" align="right"/>

```bash
┌──(nullsec㉿arch)-[~]
└─$ whoami

  name        :  Adithya Poojary
  location    :  India
  education   :  BE CSE — AI/ML Specialization, 2nd Year
                 Alva's Institute of Engineering & Technology
  background  :  Cybersecurity since Grade 7
  currently   :  Founder — AI Security Platform (Live)
```

<br/>

Offensive security researcher and AI systems builder based in India. I've been doing this since I was 12 — long before it became a career path.

I work at the intersection of security and AI: building local-first AI tooling, researching vulnerabilities across web and application layers, and currently developing an agentic code auditing platform that's already running in production.

<br/>

**Open to** &nbsp; security consulting · research collaborations · recruiting · enterprise pilots

**Inquiries** &nbsp; [nullsec0001@proton.me](mailto:nullsec0001@proton.me)

<br clear="right"/>

<br/>

---

<br/>

<div align="center">

### — Credentials —

</div>

<br/>

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   TryHackMe           ·   Top 6% Globally                           ║
║                                                                      ║
║   US Gov Healthcare   ·   Bug Bounty  ·  Accepted                   ║
║                                                                      ║
║   Mercedes Benz       ·   Private Bug Bounty  ·  Invite Only        ║
║                                                                      ║
║   ThreatScope         ·   Founder  ·  Live in Production            ║
║                                                                      ║
║   AIET                ·   BE CSE  ·  AI/ML  ·  2nd Year             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>

<br/>

---

<br/>

<div align="center">

### — Projects —

</div>

<br/>

#### ThreatScope &nbsp;·&nbsp; Founder & Lead Engineer

`Local Agentic AI` &nbsp;·&nbsp; `Code Security` &nbsp;·&nbsp; `Privacy-First`

A 100% local multi-agent AI code auditing platform. Source code never leaves the machine — built specifically for teams and companies who can't afford to send proprietary code to external APIs.

The platform runs a layered analysis pipeline combining deterministic tools (linters, dependency scanners, secret detectors) with a probabilistic multi-agent AI crew that reasons about business logic, architecture, and race conditions — things static analysis fundamentally cannot catch.

<br/>

| Layer | Component | Function |
|:---|:---|:---|
| Defense | Security Guard Agent | Pre-flight prompt injection triage |
| Deterministic | OSV Scanner | Offline CVE matching — PyPI, npm, Go, Maven, Rust |
| Deterministic | Regex / API Tools | Hardcoded secret and endpoint extraction |
| Probabilistic | Summarizer | Global code intent and logic mapping |
| Probabilistic | Syntax Reviewer | Architecture and modularity analysis |
| Probabilistic | Logic Analyzer | Business logic flaws and race condition detection |
| Probabilistic | Orchestrator | Final output assembly and Pydantic validation |
| Presentation | HTML Reporter | Visual dashboard with code health scores and charts |

<br/>

Currently in an active pilot on a live online compiler platform, processing thousands of untrusted code submissions daily.

`Python` &nbsp;·&nbsp; `CrewAI` &nbsp;·&nbsp; `Ollama (qwen2.5:7b)` &nbsp;·&nbsp; `asyncio` &nbsp;·&nbsp; `Pydantic` &nbsp;·&nbsp; `Jinja2` &nbsp;·&nbsp; `Flake8` &nbsp;·&nbsp; `ESLint`

> Pilot and partnership inquiries: [nullsec0001@proton.me](mailto:nullsec0001@proton.me)

<br/>

---

<br/>

#### [ScribbleFlow](https://github.com/NullSecurity07/ScribbleFlow) &nbsp;·&nbsp; Creator

`AI Automation` &nbsp;·&nbsp; `Local LLMs` &nbsp;·&nbsp; `Content Pipelines`

Terminal-based blog automation pipeline. Given a topic, tone, audience, and word count — it researches the web, drafts sections using a local LLM, runs SEO enhancement, and exports clean markdown. Entirely offline via Ollama, no API key required.

Architecture is modular by design — `research.py`, `writer.py`, and `prompts.py` are discrete, independently swappable units. The prompt layer is separated from the execution layer intentionally, making model-swapping a one-line config change.

`Python` &nbsp;·&nbsp; `Ollama` &nbsp;·&nbsp; `BeautifulSoup` &nbsp;·&nbsp; `DuckDuckGo Search` &nbsp;·&nbsp; `Markdown`

<br/>

---

<br/>

#### [WR4TH](https://github.com/NullSecurity07/WR4TH) &nbsp;·&nbsp; Red Team Research

`Windows Internals` &nbsp;·&nbsp; `AV Evasion` &nbsp;·&nbsp; `Offensive Tradecraft`

Documented research into Windows Defender evasion at the payload delivery layer. Implements a cross-layer delivery chain — Python controller, PowerShell stager, Batch dropper — with an out-of-band SMTP exfiltration channel for credential delivery and persistent SSH-based remote access.

The accompanying writeup covers AMSI internals, how Defender's behavioural detection works, what the bypass exploits, and mitigation recommendations from both sides of the attack.

`Python` &nbsp;·&nbsp; `PowerShell` &nbsp;·&nbsp; `AMSI` &nbsp;·&nbsp; `Batch`

> Authorized red team and educational use only.

<br/>

---

<br/>

<div align="center">

### — Stack —

</div>

<br/>

**Languages** &nbsp;&nbsp; Python · JavaScript · PowerShell · Bash · SQL

**AI / ML** &nbsp;&nbsp; Ollama · CrewAI · LLM Pipelines · Prompt Engineering · Multi-Agent Systems · RAG

**Security** &nbsp;&nbsp; Burp Suite · Nmap · Metasploit · Ghidra · Wireshark · OSINT

**Platforms** &nbsp;&nbsp; Arch Linux · Git · Docker · PyQt5 · FFmpeg · GeoIP2

<br/>

---

<br/>

<div align="center">

### — Bug Bounty —

</div>

<br/>

<div align="center">

| Program | Severity | Status |
|:---|:---|:---|
| US Government Healthcare CMS | P5 | Accepted |
| Mercedes Benz *(Private Program)* | — | Active · Invite Only |

</div>

<br/>

---

<br/>

<div align="center">

### — Statistics —

</div>

<br/>

<div align="center">

<img src="https://streak-stats.demolab.com?user=NullSecurity07&hide_border=true&background=0a0e17&ring=00b4d8&fire=00b4d8&currStreakLabel=ffffff&sideLabels=555555&dates=555555&stroke=0d1b2a&currStreakNum=ffffff&sideNums=ffffff" alt="GitHub Streak"/>

<br/><br/>

<img src="https://github-readme-stats.vercel.app/api?username=NullSecurity07&show_icons=true&bg_color=0a0e17&title_color=00b4d8&icon_color=90e0ef&text_color=888888&border_color=0d1b2a" height="155"/>
&nbsp;&nbsp;
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=NullSecurity07&layout=compact&bg_color=0a0e17&title_color=00b4d8&text_color=888888&border_color=0d1b2a" height="155"/>

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=NullSecurity07&bg_color=0a0e17&color=555555&line=00b4d8&point=90e0ef&area=true&area_color=00b4d8&hide_border=true&custom_title=Contribution%20Graph" width="100%"/>

</div>

<br/>

---

<div align="center">

<br/>

*Building at the intersection of offensive security and artificial intelligence.*

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00b4d8,50:0d1b2a,100:0a0e17&height=120&section=footer&animation=fadeIn" width="100%"/>

</div>
