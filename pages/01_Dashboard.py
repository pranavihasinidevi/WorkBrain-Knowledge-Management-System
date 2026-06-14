"""📊 Dashboard — LegacyOS"""
import streamlit as st
import plotly.graph_objects as go
from data import KNOWLEDGE, EMPLOYEES, ANNOUNCEMENTS, DEPARTMENTS, DEPT_COLORS, COMPANY_RISK, AVG_CONC

# Hide default Streamlit page navigation
st.markdown("""
<style>
[data-testid="stSidebarNav"] {display: none;}
header {visibility: hidden;}
footer {visibility: hidden;}

.block-container {
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
    max-width: 1300px;
}

div[data-testid="stMetric"] {
    background: #171827;
    padding: 24px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.05);
}

div[data-testid="stMetricLabel"] {
    color: #A1A1AA;
}

div[data-testid="stMetricValue"] {
    color: #FFFFFF;
    font-size: 34px;
    font-weight: 800;
}

div[data-testid="stMetricDelta"] {
    color: #10B981;
}

.chart-card {
    background: #11131F;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.06);
}

.wb-badge {
    display:inline-block;
    padding:4px 10px;
    border-radius:999px;
    font-size:11px;
    font-weight:700;
    margin-right:6px;
}
</style>
""", unsafe_allow_html=True)

# Header
top1, top2 = st.columns([4, 1])

with top1:
    st.markdown("""
    <h1 style="font-family:Inter,sans-serif;font-size:52px;font-weight:900;margin-bottom:6px;color:white;">
        Good morning, Arjun 👋
    </h1>
    <p style="color:#94A3B8;font-size:18px;margin-bottom:28px;">
        Your company knowledge health at a glance.
    </p>
    """, unsafe_allow_html=True)

with top2:
    st.markdown("""
    <div style="background:#171827;padding:16px 22px;border-radius:12px;
    color:white;text-align:center;font-weight:700;margin-top:8px;">
        2025/05/26
    </div>
    """, unsafe_allow_html=True)

verified = len([k for k in KNOWLEDGE if k["verified"]])

# KPI Cards
c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("📋 Knowledge Entries", len(KNOWLEDGE), "↗ 8% from last month")
c2.metric("👥 Employees", len(EMPLOYEES), "↗ 6 departments")
c3.metric("✅ Verified", verified, "↗ Manager approved")
c4.metric("⭐ Avg Rating", "4.5★", "↗ Top rated: 4.9")
c5.metric("🛡️ Avg Risk", f"{AVG_CONC}%", "↗ Concentration")

st.markdown("<br>", unsafe_allow_html=True)

# Charts Row
col1, col2 = st.columns(2)

with col1:
    dept_counts = {d: len([k for k in KNOWLEDGE if k["dept"] == d]) for d in DEPARTMENTS}

    fig = go.Figure(go.Bar(
        x=list(dept_counts.keys()),
        y=list(dept_counts.values()),
        marker_color=[DEPT_COLORS[d] for d in dept_counts],
        marker_line_width=0
    ))

    fig.update_layout(
        title=dict(
            text="📊 Department Contributions",
            font=dict(color="#F8FAFC", size=18, family="Inter")
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1", family="Inter"),
        xaxis=dict(showgrid=False, tickfont=dict(color="#CBD5E1")),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,.08)",
            tickfont=dict(color="#CBD5E1")
        ),
        margin=dict(l=0, r=0, t=50, b=0),
        height=340
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
    trend = [28, 48, 43, 60, 75, 88, 110, 135]

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=months,
        y=trend,
        mode="lines+markers",
        line=dict(color="#7C3AED", width=4),
        marker=dict(size=8, color="#8B5CF6", line=dict(color="white", width=2)),
        fill="tozeroy",
        fillcolor="rgba(124,58,237,0.25)"
    ))

    fig2.update_layout(
        title=dict(
            text="📈 Knowledge Growth Trend (Monthly)",
            font=dict(color="#F8FAFC", size=18, family="Inter")
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1", family="Inter"),
        xaxis=dict(showgrid=False, tickfont=dict(color="#CBD5E1")),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,.08)",
            tickfont=dict(color="#CBD5E1")
        ),
        margin=dict(l=0, r=0, t=50, b=0),
        height=340
    )

    st.plotly_chart(fig2, use_container_width=True)

# Bottom Row
b1, b2 = st.columns(2)

with b1:
    st.markdown("### 🔥 Most Viewed Solutions")

    top5 = sorted(KNOWLEDGE, key=lambda x: x["views"], reverse=True)[:5]

    for i, k in enumerate(top5, 1):
        dc = DEPT_COLORS.get(k["dept"], "#6366F1")

        st.markdown(f"""
        <div style="padding:14px 0;border-bottom:1px solid rgba(255,255,255,.06);">
            <span style="font-size:24px;font-weight:900;color:#7C3AED;">#{i}</span>
            <span style="font-size:17px;font-weight:800;color:#F8FAFC;margin-left:14px;">
                {k["title"]}
            </span>
            <div style="margin-left:52px;margin-top:8px;">
                <span class="wb-badge" style="background:{dc}22;color:{dc};">{k["dept"]}</span>
                <span class="wb-badge" style="background:#27272A;color:#D4D4D8;">Problem/Solution</span>
                <span style="font-size:13px;color:#94A3B8;">👁 {k["views"]} views</span>
                <span style="font-size:13px;color:#F59E0B;margin-left:8px;">{k["rating"]}★</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

with b2:
    st.markdown("### 📢 Recent Announcements")

    pc_map = {
        "Urgent": "#EF4444",
        "High": "#F59E0B",
        "Normal": "#10B981",
        "Low": "#94A3B8"
    }

    for a in ANNOUNCEMENTS[:4]:
        pc = pc_map.get(a["priority"], "#6366F1")

        st.markdown(f"""
        <div style="padding:16px 0;border-bottom:1px solid rgba(255,255,255,.06);">
            <span class="wb-badge" style="background:{pc}22;color:{pc};">
                {a["priority"]}
            </span>
            <span style="float:right;color:#64748B;font-size:12px;">
                {a["date"]}
            </span>
            <p style="font-size:16px;font-weight:800;margin:10px 0 6px;color:#F8FAFC;">
                {a["title"]}
            </p>
            <p style="font-size:14px;color:#94A3B8;margin:0;">
                {a.get("body", "Company update shared with all employees.")}
            </p>
        </div>
        """, unsafe_allow_html=True)

# Risk Alert
if COMPANY_RISK == "High":
    st.error("🚨 High Knowledge Risk Detected — Open Knowledge Risk Score for department breakdown.")