"""📊 Dashboard — WorkBrain"""
import streamlit as st
import plotly.graph_objects as go
from data import KNOWLEDGE, EMPLOYEES, ANNOUNCEMENTS, DEPARTMENTS, DEPT_COLORS, COMPANY_RISK, AVG_CONC

st.markdown('<h1 style="font-family:Syne,sans-serif;font-weight:800;margin-bottom:4px">Good morning, Arjun 👋</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#94A3B8;font-size:14px;margin-bottom:22px">Your company knowledge health at a glance.</p>', unsafe_allow_html=True)

verified = len([k for k in KNOWLEDGE if k["verified"]])

# ── KPI row ────────────────────────────────────────────────────────────────────
c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("📚 Knowledge Entries", len(KNOWLEDGE), "total entries")
c2.metric("👤 Employees",         len(EMPLOYEES), "6 departments")
c3.metric("✅ Verified",          verified,        "manager approved")
c4.metric("⭐ Avg Rating",       "4.5★",          "top rated: 4.9")
c5.metric("🛡️ Avg Risk",        f"{AVG_CONC}%",  "concentration")

st.markdown("---")

# ── Charts ─────────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    dept_counts = {d: len([k for k in KNOWLEDGE if k["dept"] == d]) for d in DEPARTMENTS}
    fig = go.Figure(go.Bar(
        x=list(dept_counts.keys()), y=list(dept_counts.values()),
        marker_color=[DEPT_COLORS[d] for d in dept_counts], marker_line_width=0,
    ))
    fig.update_layout(
        title=dict(text="📊 Department Contributions", font=dict(color="#F1F5F9",size=14,family="Inter")),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94A3B8",family="Inter"),
        xaxis=dict(showgrid=False, tickfont=dict(color="#64748B")),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,.06)", tickfont=dict(color="#64748B")),
        margin=dict(l=0,r=0,t=40,b=0), height=260,
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    months = ["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar"]
    trend  = [32,45,38,61,55,89,74,92,68,103,87,120]
    fig2 = go.Figure(go.Bar(
        x=months, y=trend, marker_color="#6366F1", marker_line_width=0,
    ))
    fig2.update_layout(
        title=dict(text="📈 Knowledge Growth Trend (Monthly)", font=dict(color="#F1F5F9",size=14,family="Inter")),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94A3B8",family="Inter"),
        xaxis=dict(showgrid=False, tickfont=dict(color="#64748B")),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,.06)", tickfont=dict(color="#64748B")),
        margin=dict(l=0,r=0,t=40,b=0), height=260,
    )
    st.plotly_chart(fig2, use_container_width=True)

# ── Bottom row ─────────────────────────────────────────────────────────────────
b1, b2 = st.columns(2)

with b1:
    st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:15px;margin-bottom:12px">🔥 Most Viewed Solutions</h3>', unsafe_allow_html=True)
    top5 = sorted(KNOWLEDGE, key=lambda x: x["views"], reverse=True)[:5]
    for i, k in enumerate(top5, 1):
        dc = DEPT_COLORS.get(k["dept"], "#6366F1")
        vbadge = '<span class="wb-badge" style="background:rgba(16,185,129,.15);color:#6EE7B7">✓ Verified</span>' if k["verified"] else ""
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;padding:10px 0;
            border-bottom:1px solid rgba(255,255,255,.05)">
            <span style="font-size:12px;font-weight:800;color:#334155;width:18px">{i}</span>
            <div style="flex:1">
                <p style="font-size:13px;font-weight:600;margin:0;color:#F1F5F9">{k["title"]}</p>
                <div style="margin-top:3px">
                    <span class="wb-badge" style="background:{dc}22;color:{dc}">{k["dept"]}</span>
                    <span style="font-size:11px;color:#64748B">👁 {k["views"]} &nbsp;⭐ {k["rating"]}</span>
                    {vbadge}
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

with b2:
    st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:15px;margin-bottom:12px">📢 Recent Announcements</h3>', unsafe_allow_html=True)
    pc_map = {"Urgent":"#EF4444","High":"#F59E0B","Normal":"#6366F1","Low":"#94A3B8"}
    for a in ANNOUNCEMENTS[:4]:
        pc = pc_map.get(a["priority"],"#6366F1")
        st.markdown(f"""
        <div style="padding:10px 0;border-bottom:1px solid rgba(255,255,255,.05)">
            <span class="wb-badge" style="background:{pc}22;color:{pc}">{a["priority"]}</span>
            <p style="font-size:13px;font-weight:600;margin:4px 0 2px;color:#F1F5F9">{a["title"]}</p>
            <p style="font-size:11px;color:#475569;margin:0">{a["date"]}</p>
        </div>""", unsafe_allow_html=True)

# ── Risk alert ─────────────────────────────────────────────────────────────────
if COMPANY_RISK == "High":
    st.markdown("---")
    st.error("🚨 **High Knowledge Risk Detected** — Navigate to **🛡️ Risk Dashboard** for department breakdown and recommended actions.")
