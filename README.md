# 🧠 WorkBrain — Workforce Knowledge Retention Platform

> **"Capture Experience Before It Walks Out the Door."**

WorkBrain is an open-source **Streamlit** web application that helps organizations capture, search, and retain employee knowledge — and flags which departments are at risk of losing it.

![Python](https://img.shields.io/badge/Python-3.9+-3B82F6?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-6366F1?style=flat-square&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-10B981?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-10B981?style=flat-square)

---

## ✨ Features

| Module | Emoji | Description |
|--------|-------|-------------|
| Dashboard | 📊 | KPI cards, growth charts, top solutions, announcements |
| Knowledge Base | 🔍 | Searchable repository — problems, solutions, SOPs, lessons |
| Submit Knowledge | 📝 | Text form + voice audio upload |
| Handover Docs | 🔄 | Structured exit documentation with approval workflow |
| Announcements | 📢 | Internal comms with priority levels and read tracking |
| Teams | 👥 | Employee directory with knowledge scores and risk labels |
| Analytics | 📈 | Views, contributions, trending topics, leaderboard |
| QR Code Access | 📱 | Generate real QR codes — scan to surface knowledge instantly |
| Knowledge Risk Score | 🛡️ | **Flagship** — flags at-risk departments in real time |

---

## 🚀 Quick Start

```bash
# 1 — Clone the repo
git clone https://github.com/YOUR_USERNAME/workbrain.git
cd workbrain

# 2 — Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows

# 3 — Install dependencies
pip install -r requirements.txt

# 4 — Run
streamlit run app.py
# Opens at http://localhost:8501
```

---

## 📁 Repository Structure

```
workbrain/
├── app.py                  Main Streamlit app + shared CSS + navigation
├── data.py                 All demo data (employees, knowledge, handovers…)
├── requirements.txt        Python dependencies
├── .gitignore
├── README.md
│
├── .streamlit/
│   └── config.toml         Dark theme (#0B0F1A) + Streamlit settings
│
└── pages/
    ├── 01_Dashboard.py     📊 KPIs · charts · top solutions
    ├── 02_Knowledge.py     🔍 Search · filter · expandable cards
    ├── 03_Submit.py        📝 Text form + voice upload
    ├── 04_Handover.py      🔄 Handover list + new form
    ├── 05_Announcements.py 📢 Comms + read-rate bars
    ├── 06_Teams.py         👥 Employee directory grid
    ├── 07_Analytics.py     📈 Charts + leaderboard
    ├── 08_QR.py            📱 Real QR generation + download
    └── 09_Risk.py          🛡️ Risk Score + heatmap + at-risk list
```

---

## 🛡️ Knowledge Risk Score

```
Concentration = (Top-2 employee entries ÷ Total dept entries) × 100

> 70%    →  🔴 High Risk
45–70%  →  🟡 Medium Risk
< 45%   →  🟢 Low Risk
```

---

## 🎨 Design System

| Element | Value |
|---------|-------|
| Background | `#0B0F1A` deep navy-black |
| Card Surface | `rgba(255,255,255,0.04)` glass |
| Primary | `#6366F1` Indigo |
| Secondary | `#8B5CF6` Purple |
| Success | `#10B981` Green |
| Warning | `#F59E0B` Amber |
| Danger | `#EF4444` Red |
| Headings | **Syne** 700/800 |
| Body | **Inter** 400–700 |

---

## ☁️ Deploy to Streamlit Community Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select your repo → set `app.py` as entry point
4. Click **Deploy** — live in ~60 seconds!

---

## 📄 License

MIT — free to use, modify, and distribute.

