<div align="center">

```
███╗   ██╗██╗   ██╗██╗     ██╗      ███████╗███████╗ ██████╗
████╗  ██║██║   ██║██║     ██║      ██╔════╝██╔════╝██╔════╝
██╔██╗ ██║██║   ██║██║     ██║      ███████╗█████╗  ██║
██║╚██╗██║██║   ██║██║     ██║      ╚════██║██╔══╝  ██║
██║ ╚████║╚██████╔╝███████╗███████╗ ███████║███████╗╚██████╗
╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝ ╚══════╝╚══════╝ ╚═════╝
```

### Adithya Poojary
**Offensive Security Researcher · AI Systems Builder · Founder @ ThreatScope**

*Building at the intersection of cybersecurity and artificial intelligence.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adithya-poojary000/)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-Top_6%25-212C42?style=flat-square&logo=tryhackme&logoColor=red)](https://tryhackme.com)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:)

</div>

---

## whoami

```bash
$ cat /etc/adithya/profile.conf

[identity]
role        = Security Researcher & AI Engineer
location    = India
education   = BE CSE (AI/ML Specialization) — 2nd Year
experience  = Cybersecurity since Grade 7

[credentials]
tryhackme   = Top 6% globally
bug_bounty  = Accepted finds: US Government Healthcare CMS (P5)
programs    = Invited — Private Mercedes Managed Bug Bounty
speciality  = Offensive Security · AI-Powered Tooling · OSINT
```

I've been breaking and building systems since I was 12. Today I research vulnerabilities, build AI-native security tooling, and am growing **ThreatScope** — a privacy-first, local agentic code auditing platform — into a company.

My edge: I approach security problems with an offensive mindset and solve them with AI systems. Most people in this space know one side. I work on both.

---

## 🏗️ Featured Projects

### [ThreatScope](https://github.com/NullSecurity07/ThreatScope) — *Founder & Lead Engineer*
> **Privacy-First · Local Agentic AI · Code Security**

A professional-grade, 100% local multi-agent AI code auditing platform. No code leaves your machine — ever.

- **Multi-Agent Architecture** — Specialized CrewAI agents (Summarizer → Syntax Reviewer → Logic Analyzer → Orchestrator) run in staged sequence, each enriching context for the next
- **Defense-in-Depth Prompt Injection Guard** — Pre-flight triage agent + randomized XML sandbox delimiters on every run to neutralize adversarial code payloads
- **Offline OSV Dependency Scanner** — Simultaneous CVE matching across PyPI, npm, Go (mod), Maven, and Rust (Cargo) with zero internet dependency
- **Hybrid Analysis** — Deterministic linting (Flake8, ESLint) combined with probabilistic LLM reasoning catches what either layer alone misses
- **Powered by** `qwen2.5:7b` via Ollama · CrewAI · Python asyncio · Jinja2 HTML reporting

> 🟢 **Live in production** — Active pilot securing a real-world online compiler platform, processing thousands of untrusted code submissions daily.

`Python` `CrewAI` `Ollama` `LLM` `Multi-Agent` `SAST` `AppSec` `Privacy`

---

### [ScribbleFlow](https://github.com/NullSecurity01/ScribbleFlow) — *Creator*
> **AI Automation · Local LLMs · Content Pipelines**

End-to-end blog automation pipeline: topic → live web research → LLM drafting → SEO-optimized markdown. Fully offline-capable via Ollama.

- Modular pipeline architecture (research, writing, SEO as separate concerns)
- Local LLM inference — no API key, no data leaving your machine
- Configurable tone, audience, style, and word count per run
- BeautifulSoup web scraping + DuckDuckGo research layer

`Python` `Ollama` `DeepSeek` `BeautifulSoup` `LLM Pipelines` `Automation`

---

### [WR4TH](https://github.com/NullSecurity01/WR4TH) — *Creator*
> **Offensive Security · Windows Internals · AV Evasion**

A Linux-controlled, network-based remote access framework for Windows environments — built to understand and demonstrate Windows Defender evasion techniques.

- Cross-layer payload delivery: Python controller + PowerShell stager + Batch dropper
- Out-of-band SMTP exfiltration channel via Mailtrap
- Persistent SSH-based remote access with file upload/download/execute
- Built for authorized red team and educational lab environments

`Python` `PowerShell` `Batch` `AV Evasion` `RAT` `Red Team` `Windows Internals`

---

## 🔬 Research & Bug Bounty

| Program | Finding | Severity | Status |
|---|---|---|---|
| US Government Healthcare CMS | Vulnerability disclosure | P5 | ✅ Accepted |
| Mercedes (Private Program) | Active — Invite Only | — | 🔒 Private |

---

## ⚙️ Technical Stack

```
Languages     Python · PowerShell · Bash · JavaScript · SQL
AI/ML         Ollama · CrewAI · LLM Pipelines · Prompt Engineering
              Local Inference · Multi-Agent Systems · RAG
Security      OSINT · Web App Pentesting · Network Security
              AV Evasion · SAST · Threat Modeling · Bug Bounty
Tools         Burp Suite · Nmap · Metasploit · Ghidra · Wireshark
              FFmpeg · GeoIP2 · Flake8 · ESLint
Platforms     Arch Linux (daily driver) · Windows · TryHackMe
              HackerOne · GitHub Actions
Hardware      Lenovo IdeaPad · Ryzen 7 · RTX 3050 · 32GB RAM
```

---

## 📈 Focus Areas (2025–2026)

- **AI Security** — Adversarial ML, prompt injection, LLM pipeline hardening
- **ThreatScope** — Growing from pilot to product: CI/CD integrations, multi-language support, team features
- **Bug Bounty** — Expanding scope: web, API, and AI-surface targets
- **Research** — Publishing offensive security and AI/security intersection writeups

---

## 🧠 Philosophy

> *"Security is a systems problem. AI is a reasoning layer. The people who understand both will define what the next decade looks like."*

I build tools I'd want to exist. I research what I'd want to understand. I don't separate the offensive and defensive mindsets — both make you sharper.

---

<div align="center">

**Open to:** Research collaborations · Security consulting · Early-stage advisory · Recruiting conversations

*Always reading. Always building.*

</div>
