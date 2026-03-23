<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0e17,50:0d1b2a,100:00b4d8&height=220&section=header&text=Adithya%20Poojary&fontSize=52&fontColor=ffffff&fontAlignY=38&fontAlign=50&desc=Security%20Researcher%20%C2%B7%20AI%20Engineer%20%C2%B7%20Founder&descSize=16&descAlignY=58&descAlign=50&descColor=90e0ef&animation=fadeIn" width="100%"/>

</div>

<br/>

<div align="center">

[LinkedIn](https://www.linkedin.com/in/adithyapoojary/) &nbsp;&nbsp;·&nbsp;&nbsp; [TryHackMe](https://tryhackme.com/p/nullsec0001) &nbsp;&nbsp;·&nbsp;&nbsp; [nullsec0001@proton.me](mailto:nullsec0001@proton.me) &nbsp;&nbsp;·&nbsp;&nbsp; [thisisadithya07@gmail.com](mailto:thisisadithya07@gmail.com)

</div>

<br/><br/>

---

<br/>

<div align="center">

### — Who I Am —

</div>

<br/>

<img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="170" align="right"/>

```bash
┌──(nullsec㉿arch)-[~]
└─$ whoami

  name        :  Adithya Poojary
  location    :  India
  education   :  BE CSE — AI/ML Specialization, 2nd Year
                 Alva's Institute of Engineering & Technology
  background  :  Cybersecurity since Grade 7 (age ~12)
  currently   :  Founder — AI Security Platform (Live)
```

<br/>

I've been breaking and building systems since I was 12. Most people my age are still following tutorials. I've already shipped a production security platform, found vulnerabilities in US government infrastructure, and earned a private invite to Mercedes Benz's managed bug bounty program — all before finishing my second year of college.

I work at the intersection of offensive security and AI. I don't just use AI tools — I build them, harden them, and understand how they fail.

<br/>

> **Open to** &nbsp; Security consulting · Research collaborations · Recruiting · Enterprise pilots
>
> **Inquiries** &nbsp; [nullsec0001@proton.me](mailto:nullsec0001@proton.me)

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
║   TryHackMe  ·  Top 6% Globally                                      ║
║                                                                      ║
║   Bug Bounty  ·  US Government Healthcare CMS  ·  Accepted           ║
║                                                                      ║
║   Bug Bounty  ·  Mercedes Benz  ·  Private Program  ·  Invite Only   ║
║                                                                      ║
║   Founder  ·  AI Security Platform  ·  Live in Production            ║
║                                                                      ║
║   Student  ·  BE CSE  ·  AI/ML Specialization  ·  2nd Year           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>

<br/>

The credentials above are not aspirational. TryHackMe ranks globally across hundreds of thousands of users. The US Government and Mercedes Benz programs are real, accepted, production programs — not CTF exercises. The platform is deployed and processing live traffic. All of this happened before my 19th birthday.

<br/>

---

<br/>

<div align="center">

### — Projects —

</div>

<br/>

#### ThreatScope &nbsp;·&nbsp; Founder & Lead Engineer

> Privacy-First &nbsp;·&nbsp; Local Agentic AI &nbsp;·&nbsp; Code Security &nbsp;·&nbsp; **Live in Production**

The problem: modern code security tools are either *dumb but private* (static linters) or *smart but invasive* (cloud LLMs that read your proprietary code). No good middle ground existed.

ThreatScope is that middle ground — a 100% local, multi-agent AI code auditing platform. Your source code never leaves your machine. It combines deterministic analysis with probabilistic LLM reasoning to catch what either layer alone misses.

<br/>

| Layer | Component | What it does |
|:---|:---|:---|
| Defense | Security Guard Agent | Intercepts adversarial prompt injection payloads before the main run |
| Deterministic | OSV Dependency Scanner | Offline CVE matching across PyPI, npm, Go, Maven, and Rust simultaneously |
| Deterministic | Regex / API Tools | Extracts hardcoded secrets, tokens, and exposed endpoints |
| Probabilistic | Summarizer | AI agent that maps contextual logic and global code intent |
| Probabilistic | Syntax Reviewer | AI agent auditing modularity, architecture, and code structure |
| Probabilistic | Logic Analyzer | AI red-teamer targeting business logic flaws and race conditions |
| Probabilistic | Orchestrator | QC agent assembling final output into a validated Pydantic object |
| Presentation | HTML Reporter | Auto-generated visual dashboard with code health scores and charts |

<br/>

**Why it matters:** Enterprise code security tools (Veracode, Checkmarx, Snyk) cost $30–100K+ per year and require cloud access. ThreatScope offers comparable AI-powered analysis at zero data-leakage risk — a gap the market hasn't properly addressed.

**Status:** Actively piloting on a live LeetCode-style online compiler platform. Processing thousands of untrusted code submissions daily in production.

`Python` &nbsp;·&nbsp; `CrewAI` &nbsp;·&nbsp; `Ollama (qwen2.5:7b)` &nbsp;·&nbsp; `asyncio` &nbsp;·&nbsp; `Pydantic` &nbsp;·&nbsp; `Jinja2` &nbsp;·&nbsp; `Flake8` &nbsp;·&nbsp; `ESLint`

> Pilot and partnership inquiries: [nullsec0001@proton.me](mailto:nullsec0001@proton.me)

<br/>

---

<br/>

#### [ScribbleFlow](https://github.com/NullSecurity07/ScribbleFlow) &nbsp;·&nbsp; Creator

> AI Automation &nbsp;·&nbsp; Local LLMs &nbsp;·&nbsp; Content Pipelines

End-to-end blog automation pipeline — from a raw topic to a fully researched, LLM-drafted, SEO-optimized markdown post — entirely from the terminal, entirely offline.

The architecture is modular by design: web research, LLM drafting, and prompt logic are discrete, swappable components. Uses Ollama for local inference so no API key or data exposure is required. Configurable tone, audience, writing style, and word count per run.

`Python` &nbsp;·&nbsp; `Ollama` &nbsp;·&nbsp; `BeautifulSoup` &nbsp;·&nbsp; `DuckDuckGo Search` &nbsp;·&nbsp; `Markdown`

<br/>

---

<br/>

#### [WR4TH](https://github.com/NullSecurity07/WR4TH) &nbsp;·&nbsp; Red Team Research

> Windows Internals &nbsp;·&nbsp; AV Evasion Research &nbsp;·&nbsp; Offensive Tradecraft

Documented research into Windows Defender evasion mechanisms at the payload delivery layer. Built to understand how attackers operate — because defenders who haven't studied offense miss entire attack classes.

The project implements a cross-layer delivery chain (Python controller → PowerShell stager → Batch dropper), an out-of-band SMTP exfiltration channel, and a persistent SSH access mechanism. The accompanying writeup covers AMSI internals, detection logic, bypass techniques, and mitigation recommendations from both attacker and defender perspectives.

`Python` &nbsp;·&nbsp; `PowerShell` &nbsp;·&nbsp; `Windows Internals` &nbsp;·&nbsp; `AMSI` &nbsp;·&nbsp; `Batch`

> For educational and authorized red team use only.

<br/>

---

<br/>

<div align="center">

### — Stack —

</div>

<br/>

**Languages** &nbsp;&nbsp; Python &nbsp;·&nbsp; JavaScript &nbsp;·&nbsp; PowerShell &nbsp;·&nbsp; Bash &nbsp;·&nbsp; SQL

**AI / ML** &nbsp;&nbsp; Ollama &nbsp;·&nbsp; CrewAI &nbsp;·&nbsp; LLM Pipelines &nbsp;·&nbsp; Prompt Engineering &nbsp;·&nbsp; Multi-Agent Systems &nbsp;·&nbsp; RAG

**Security** &nbsp;&nbsp; Burp Suite &nbsp;·&nbsp; Nmap &nbsp;·&nbsp; Metasploit &nbsp;·&nbsp; Ghidra &nbsp;·&nbsp; Wireshark &nbsp;·&nbsp; OSINT

**Platforms** &nbsp;&nbsp; Arch Linux &nbsp;·&nbsp; Git &nbsp;·&nbsp; Docker &nbsp;·&nbsp; PyQt5 &nbsp;·&nbsp; FFmpeg &nbsp;·&nbsp; GeoIP2

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
| Mercedes Benz *(Private Program)* | — | Active &nbsp;·&nbsp; Invite Only |

</div>

<br/>

Both of these are real programs with real security teams. The Mercedes program is invitation-only — access is granted based on demonstrated skill and reputation, not open registration.

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

<br/>

<div align="center">

*Building at the intersection of offensive security and artificial intelligence.*

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00b4d8,50:0d1b2a,100:0a0e17&height=120&section=footer&animation=fadeIn" width="100%"/>

</div>
