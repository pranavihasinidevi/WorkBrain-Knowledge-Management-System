# LegacyOS — Knowledge Continuity Platform

> "Don't lose the brain when you lose the person."

## What changed (WorkBrain → LegacyOS)

| # | What | File |
|---|------|------|
| 1 | App name → **LegacyOS** | `app.py` |
| 2 | page_title → `"LegacyOS"` | `app.py` |
| 3 | page_icon → your orbital logo PNG | `app.py` |
| 4 | Sidebar: **Legacy**`OS` two-tone name | `app.py` |
| 5 | Sidebar: orbital logo image | `app.py` |
| 6 | Dashboard title font → clean Inter 36px | `pages/dashboard.py` |
| 7 | Metric cards → full labels + correct emojis | `pages/dashboard.py` |
| 8 | Growth chart → smooth purple area/line chart | `pages/dashboard.py` |
| 9 | Date picker added top-right | `pages/dashboard.py` |
| 10 | User profile (AD / Arjun D. / Admin) at sidebar bottom | `app.py` |
| 11 | Streamlit theme → dark purple palette | `.streamlit/config.toml` |

## Setup

```bash
# 1. Copy these files into your existing project

# 2. Drop your orbital logo PNG here:
#    assets/logo.png

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
streamlit run app.py
```

## File structure

```
legacyos/
├── app.py                    ← CHANGED: name, logo, sidebar, user profile
├── requirements.txt          ← dependencies
├── README.md
├── assets/
│   └── logo.png              ← PUT YOUR ORBITAL LOGO HERE
├── .streamlit/
│   └── config.toml           ← CHANGED: dark purple theme
└── pages/
    ├── __init__.py
    └── dashboard.py          ← CHANGED: title, metrics, area chart, date picker
```

## Push to GitHub

```bash
git add .
git commit -m "rebrand: WorkBrain → LegacyOS — logo, fonts, area chart, user profile"
git push origin main
```

## GitHub repo rename

1. Go to your repo on GitHub
2. Settings → General → Repository name
3. Change to `legacyos`
4. Click **Rename**
5. Update your local remote:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/legacyos.git
git remote -v   # verify
```
