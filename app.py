"""
LegacyOS — Workforce Knowledge Retention Platform
Run: streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="LegacyOS",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #0B0F1A;
}

[data-testid="stSidebarNav"] {
    display: none;
}

header, footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
    max-width: 1350px;
}

section[data-testid="stSidebar"] {
    background: #171827 !important;
    border-right: 1px solid rgba(255,255,255,.08);
}

section[data-testid="stSidebar"] .stRadio label {
    color: #CBD5E1 !important;
    font-size: 15px !important;
    font-weight: 500 !important;
}

div[data-testid="stMetric"] {
    background: #171827 !important;
    padding: 24px !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,.06) !important;
}

div[data-testid="stMetricValue"] {
    color: white !important;
    font-size: 34px !important;
    font-weight: 900 !important;
}

div[data-testid="stMetricLabel"] {
    color: #A1A1AA !important;
}

div[data-testid="stMetricDelta"] {
    color: #10B981 !important;
}

.wb-badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    margin-right: 6px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:14px;padding:18px 8px 28px;">
        <div style="width:46px;height:46px;border-radius:12px;
            background:linear-gradient(135deg,#6366F1,#8B5CF6);
            display:flex;align-items:center;justify-content:center;font-size:24px;">
            🌉
        </div>
        <div>
            <p style="font-size:24px;font-weight:900;color:white;margin:0;">
                Legacy<span style="color:#8B5CF6;">OS</span>
            </p>
            <p style="font-size:13px;color:#64748B;margin:0;">
                Knowledge Platform
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "📊 Dashboard",
            "🔍 Knowledge Base",
            "📝 Submit Knowledge",
            "🔄 Handover Docs",
            "📢 Announcements",
            "👥 Teams",
            "📈 Analytics",
            "📱 QR Code Access",
            "🛡️ Risk Dashboard",
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("""
    <p style="font-size:12px;color:#64748B;margin-top:20px;">
        Every employee leaves.<br>
        Their knowledge doesn't.
    </p>
    """, unsafe_allow_html=True)

PAGE_MAP = {
    "📊 Dashboard": "pages/01_Dashboard.py",
    "🔍 Knowledge Base": "pages/02_Knowledge.py",
    "📝 Submit Knowledge": "pages/03_Submit.py",
    "🔄 Handover Docs": "pages/04_Handover.py",
    "📢 Announcements": "pages/05_Announcements.py",
    "👥 Teams": "pages/06_Teams.py",
    "📈 Analytics": "pages/07_Analytics.py",
    "📱 QR Code Access": "pages/08_QR.py",
    "🛡️ Risk Dashboard": "pages/09_Risk.py",
}

with open(PAGE_MAP[page], encoding="utf-8") as f:
    exec(
        compile(f.read(), PAGE_MAP[page], "exec"),
        {
            "__name__": "__main__",
            "st": st,
        }
    )