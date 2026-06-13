"""
WorkBrain — Workforce Knowledge Retention Platform
===================================================
Streamlit multi-page app.  Run:  streamlit run app.py

Design System
  Background  : #0B0F1A  (deep navy-black)
  Accent      : #6366F1  (Indigo)  +  #8B5CF6  (Purple)
  Success     : #10B981  |  Warning: #F59E0B  |  Danger: #EF4444
  Headings    : Syne 700/800   |   Body: Inter 400-700
  Emojis      : one per module, functional (📊🔍📝🔄📢👥📈📱🛡️)
"""

import streamlit as st
import importlib, sys, types

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="WorkBrain",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global design-system CSS ───────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Syne:wght@700;800&display=swap');

/* base */
html,body,[class*="css"]{ font-family:'Inter',sans-serif!important; }
h1,h2,h3,.syne{ font-family:'Syne',sans-serif!important; font-weight:800!important; }

/* sidebar */
section[data-testid="stSidebar"]{
    background-color:#0F1629!important;
    border-right:1px solid rgba(255,255,255,.07)!important;
}
section[data-testid="stSidebar"] .stRadio label{
    font-family:'Inter',sans-serif!important;
    font-size:13px!important;
    color:#94A3B8!important;
    padding:6px 0!important;
}
section[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]{
    gap:4px!important;
}

/* metrics */
div[data-testid="stMetric"]{
    background:rgba(255,255,255,.04)!important;
    border:1px solid rgba(255,255,255,.09)!important;
    border-radius:14px!important;
    padding:16px 18px!important;
}
div[data-testid="stMetricValue"]{
    font-family:'Syne',sans-serif!important;
    font-size:26px!important;
    font-weight:800!important;
}
div[data-testid="stMetricLabel"]{
    color:#94A3B8!important;
    font-size:12px!important;
}
div[data-testid="stMetricDelta"]{
    font-size:11px!important;
}

/* primary button */
.stButton>button{
    background:linear-gradient(135deg,#6366F1,#8B5CF6)!important;
    color:#fff!important; border:none!important;
    border-radius:9px!important;
    font-family:'Inter',sans-serif!important;
    font-weight:600!important;
}
.stButton>button:hover{ opacity:.88!important; }

/* download button */
.stDownloadButton>button{
    background:rgba(255,255,255,.05)!important;
    color:#94A3B8!important;
    border:1px solid rgba(255,255,255,.12)!important;
    border-radius:9px!important;
}

/* inputs */
.stTextInput>div>div>input,
.stTextArea>div>div>textarea{
    background:rgba(255,255,255,.07)!important;
    border:1px solid rgba(255,255,255,.09)!important;
    border-radius:8px!important;
    color:#F1F5F9!important;
    font-family:'Inter',sans-serif!important;
}
.stSelectbox>div>div{
    background:rgba(255,255,255,.07)!important;
    border:1px solid rgba(255,255,255,.09)!important;
    border-radius:8px!important;
}
.stSelectbox label,.stTextInput label,.stTextArea label{
    color:#94A3B8!important; font-size:12px!important; font-weight:600!important;
}

/* expanders */
.streamlit-expanderHeader{
    background:rgba(255,255,255,.04)!important;
    border:1px solid rgba(255,255,255,.09)!important;
    border-radius:10px!important;
    color:#F1F5F9!important;
    font-family:'Inter',sans-serif!important;
    font-weight:600!important;
}

/* tabs */
.stTabs [data-baseweb="tab"]{
    color:#64748B!important;
    font-family:'Inter',sans-serif!important;
    font-weight:500!important;
}
.stTabs [aria-selected="true"]{
    color:#A5B4FC!important;
    border-bottom-color:#6366F1!important;
}
.stTabs [data-baseweb="tab-list"]{
    background:transparent!important;
    border-bottom:1px solid rgba(255,255,255,.07)!important;
}

/* progress */
.stProgress>div>div{ background:#6366F1!important; }

/* divider */
hr{ border-color:rgba(255,255,255,.07)!important; }

/* card utility classes */
.wb-card{
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.09);
    border-radius:16px; padding:20px; margin-bottom:12px;
}
.wb-badge{
    display:inline-block; padding:3px 10px; border-radius:20px;
    font-size:11px; font-weight:600; margin-right:4px;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar nav ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:10px;padding:10px 0 20px">
        <div style="width:34px;height:34px;border-radius:9px;
            background:linear-gradient(135deg,#6366F1,#8B5CF6);
            display:flex;align-items:center;justify-content:center;font-size:18px">🧠</div>
        <div>
            <p style="font-family:'Syne',sans-serif;font-size:17px;font-weight:800;
                color:#F1F5F9;margin:0">WorkBrain</p>
            <p style="font-size:10px;color:#334155;margin:0">Knowledge Platform</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio("nav", [
        "📊  Dashboard",
        "🔍  Knowledge Base",
        "📝  Submit Knowledge",
        "🔄  Handover Docs",
        "📢  Announcements",
        "👥  Teams",
        "📈  Analytics",
        "📱  QR Code Access",
        "🛡️  Risk Dashboard",
    ], label_visibility="collapsed")

    st.markdown("---")
    st.markdown("""
    <p style="font-size:10px;color:#1E293B;margin:0">WorkBrain v2.0 · Streamlit</p>
    <p style="font-size:10px;color:#1E293B;margin:3px 0 0">
    "Capture Experience Before It<br>Walks Out the Door."</p>
    """, unsafe_allow_html=True)

# ── Route to page module ───────────────────────────────────────────────────────
PAGE_MAP = {
    "📊  Dashboard":        "pages/01_Dashboard.py",
    "🔍  Knowledge Base":   "pages/02_Knowledge.py",
    "📝  Submit Knowledge": "pages/03_Submit.py",
    "🔄  Handover Docs":    "pages/04_Handover.py",
    "📢  Announcements":    "pages/05_Announcements.py",
    "👥  Teams":            "pages/06_Teams.py",
    "📈  Analytics":        "pages/07_Analytics.py",
    "📱  QR Code Access":   "pages/08_QR.py",
    "🛡️  Risk Dashboard":   "pages/09_Risk.py",
}

with open(PAGE_MAP[page], encoding="utf-8") as f:
    exec(compile(f.read(), PAGE_MAP[page], "exec"), {
        "__name__": "__main__",
        "st": st,
    })
