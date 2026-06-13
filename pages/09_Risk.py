"""🛡️ Knowledge Risk Score — WorkBrain Flagship Feature"""
import streamlit as st
import plotly.graph_objects as go
from data import DEPARTMENTS, DEPT_COLORS, EMPLOYEES, KNOWLEDGE, RISK_STATS, COMPANY_RISK, AVG_CONC

st.markdown("""
<div style="display:flex;align-items:center;gap:12px;margin-bottom:4px">
    <h1 style="font-family:Syne,sans-serif;font-weight:800;margin:0">🛡️ Knowledge Risk Score</h1>
    <span class="wb-badge" style="background:rgba(16,185,129,.2);color:#6EE7B7;font-size:12px">Flagship Feature</span>
</div>""", unsafe_allow_html=True)
st.markdown("""<p style="color:#94A3B8;margin-bottom:6px">Identify departments at risk of losing critical knowledge if key employees leave.</p>
<p style="font-size:13px;color:#64748B;margin-bottom:20px">
    <strong style="color:#94A3B8">Formula:</strong>
    (Top-2 employee entries ÷ Total dept entries) × 100 = Concentration %
</p>""", unsafe_allow_html=True)

RC = {"High":"#EF4444","Medium":"#F59E0B","Low":"#10B981"}
rc = RC.get(COMPANY_RISK,"#10B981")

# ── Company banner ─────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="background:{rc}18;border:1px solid {rc}40;border-radius:14px;
    padding:22px 26px;margin-bottom:20px">
    <p style="font-size:12px;color:#94A3B8;margin:0 0 4px">Overall Company Knowledge Risk</p>
    <p style="font-family:Syne,sans-serif;font-size:38px;font-weight:800;color:{rc};margin:0">{COMPANY_RISK}</p>
    <p style="font-size:14px;color:#94A3B8;margin:6px 0 0">
        Average concentration: <strong style="color:#F1F5F9">{AVG_CONC}%</strong>
    </p>
    <p style="font-size:13px;color:#64748B;margin:4px 0 0">
        {"🚨 Critical — immediate knowledge transfer plans required." if AVG_CONC>65
        else "⚠ Moderate — some departments need attention." if AVG_CONC>45
        else "✅ Healthy — knowledge is well distributed."}
    </p>
</div>""", unsafe_allow_html=True)

# Gauge
fig_g=go.Figure(go.Indicator(
    mode="gauge+number",value=AVG_CONC,
    title={"text":"Avg Concentration %","font":{"color":"#94A3B8","size":12,"family":"Inter"}},
    gauge={
        "axis":{"range":[0,100],"tickfont":{"color":"#64748B","size":10}},
        "bar":{"color":rc},
        "bgcolor":"rgba(255,255,255,.04)",
        "steps":[{"range":[0,45],"color":"rgba(16,185,129,.07)"},
                 {"range":[45,70],"color":"rgba(245,158,11,.07)"},
                 {"range":[70,100],"color":"rgba(239,68,68,.07)"}],
        "borderwidth":0,
    },
    number={"suffix":"%","font":{"color":"#F1F5F9","size":30,"family":"Inter"}},
))
fig_g.update_layout(paper_bgcolor="rgba(0,0,0,0)",font=dict(color="#94A3B8"),
    height=220,margin=dict(l=20,r=20,t=30,b=0))
st.plotly_chart(fig_g,use_container_width=True)

st.markdown("---")
st.markdown('<h2 style="font-family:Syne,sans-serif;font-size:18px;margin-bottom:16px">Department Risk Cards</h2>', unsafe_allow_html=True)

# Dept cards  3-col
d_cols=st.columns(3)
for i,dept in enumerate(DEPARTMENTS):
    s=RISK_STATS[dept]
    col=d_cols[i%3]
    dc=DEPT_COLORS.get(dept,"#6366F1")
    r_c=RC.get(s["risk"],"#10B981")
    border=f"{r_c}45" if s["risk"]=="High" else "rgba(255,255,255,.09)"

    top3="".join(
        f'<div style="display:inline-flex;align-items:center;gap:4px;padding:3px 8px;'
        f'border-radius:8px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);margin:2px">'
        f'<span style="font-size:9px;color:#A5B4FC">{e["initials"]}</span>'
        f'<span style="font-size:11px;font-weight:700;color:{r_c}">{e["entries"]}</span></div>'
        for e in s["sorted"][:3])

    recs=""
    if s["risk"]=="High":
        recs=('<div style="margin-top:12px;padding:10px 12px;border-radius:10px;'
              'background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.2)">'
              '<p style="font-size:10px;font-weight:700;color:#FCA5A5;margin:0 0 5px">⚠ Recommended Actions</p>'
              +''.join(f'<p style="font-size:10px;color:#94A3B8;margin:2px 0">→ {a}</p>'
                       for a in ["Request handover docs","Schedule transfer session",
                                  "Record additional voice notes","Assign backup knowledge owner"])
              +'</div>')

    col.markdown(f"""
    <div style="background:rgba(255,255,255,.04);border:1px solid {border};
        border-radius:14px;padding:18px;margin-bottom:14px">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px">
            <div>
                <p style="font-family:Syne,sans-serif;font-size:15px;font-weight:700;
                    margin:0;color:#F1F5F9">{dept}</p>
                <p style="font-size:11px;color:#64748B;margin:2px 0 0">
                    {len(s["emps"])} employees · {s["total"]} entries</p>
            </div>
            <span class="wb-badge" style="background:{r_c}22;color:{r_c}">
                <span style="width:5px;height:5px;border-radius:50%;background:{r_c};
                    display:inline-block;margin-right:3px"></span>{s["risk"]} Risk
            </span>
        </div>
        <div style="display:flex;justify-content:space-between;margin-bottom:4px">
            <span style="font-size:11px;color:#94A3B8">Concentration</span>
            <span style="font-size:12px;font-weight:700;color:{r_c}">{s["concentration"]}%</span>
        </div>
        <div style="background:rgba(255,255,255,.06);border-radius:99px;height:8px;margin-bottom:6px">
            <div style="width:{s["concentration"]}%;height:8px;background:{r_c};border-radius:99px"></div>
        </div>
        <p style="font-size:10px;color:#475569;margin:0 0 8px">
            Top 2 hold {s["concentration"]}% of dept knowledge</p>
        <div style="display:flex;flex-wrap:wrap;gap:4px">{top3}</div>
        {recs}
    </div>""", unsafe_allow_html=True)

st.markdown("---")

# Heatmap + Scores
hm_col, sc_col = st.columns(2)

with hm_col:
    st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:15px;margin-bottom:8px">Knowledge Dependency Heatmap</h3>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:12px;color:#64748B;margin-bottom:10px">Entries per employee. Darker = higher concentration risk.</p>', unsafe_allow_html=True)
    se=sorted(EMPLOYEES,key=lambda x:x["entries"],reverse=True)
    names=[e["name"].split()[0] for e in se]
    vals=[e["entries"] for e in se]
    fig_hm=go.Figure(go.Heatmap(
        z=[vals],x=names,
        colorscale=[[0,"rgba(99,102,241,.07)"],[0.5,"rgba(99,102,241,.45)"],[1,"rgba(99,102,241,.95)"]],
        showscale=True,
        colorbar=dict(tickfont=dict(color="#94A3B8",size=9),
            title=dict(text="Entries",font=dict(color="#94A3B8",size=10)),thickness=12),
        hovertemplate='<b>%{x}</b><br>Entries: %{z}<extra></extra>',
    ))
    fig_hm.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94A3B8",family="Inter"),
        xaxis=dict(tickfont=dict(color="#64748B",size=9),showgrid=False),
        yaxis=dict(showticklabels=False,showgrid=False),
        margin=dict(l=0,r=0,t=10,b=0),height=160)
    st.plotly_chart(fig_hm,use_container_width=True)

with sc_col:
    st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:15px;margin-bottom:14px">Department Risk Scores</h3>', unsafe_allow_html=True)
    for dept in DEPARTMENTS:
        s=RISK_STATS[dept]
        r_c=RC.get(s["risk"],"#10B981")
        st.markdown(f"""
        <div style="margin-bottom:12px">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px">
                <span style="font-size:13px;font-weight:600;color:#F1F5F9">{dept}</span>
                <span style="font-size:13px;font-weight:700;color:{r_c}">{s["score"]}/100</span>
            </div>
            <div style="background:rgba(255,255,255,.06);border-radius:99px;height:7px">
                <div style="width:{s["score"]}%;height:7px;background:{r_c};border-radius:99px"></div>
            </div>
            <p style="font-size:10px;color:#475569;margin:2px 0 0">
                {s["risk"]} Risk · {s["concentration"]}% concentrated</p>
        </div>""", unsafe_allow_html=True)
    st.markdown("""
    <div style="padding:12px;border-radius:10px;background:rgba(255,255,255,.03);
        border:1px solid rgba(255,255,255,.07);margin-top:12px">
        <p style="font-size:11px;font-weight:700;color:#F1F5F9;margin:0 0 6px">Risk Legend</p>
        <p style="font-size:11px;margin:0 0 4px"><span style="color:#10B981">🟢 Low</span> — Score &gt; 60</p>
        <p style="font-size:11px;margin:0 0 4px"><span style="color:#F59E0B">🟡 Medium</span> — Score 40–60</p>
        <p style="font-size:11px;margin:0"><span style="color:#EF4444">🔴 High</span> — Score &lt; 40</p>
    </div>""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:15px;margin-bottom:14px">⚠ At-Risk Employees — Action Required</h3>', unsafe_allow_html=True)

at_risk=sorted([e for e in EMPLOYEES if e["risk"] in ("Critical","High")],
    key=lambda x:x["entries"],reverse=True)
ar_cols=st.columns(2)
for i,e in enumerate(at_risk):
    col=ar_cols[i%2]
    r_c="#EF4444" if e["risk"]=="Critical" else "#F59E0B"
    dt=RISK_STATS[e["dept"]]["total"]
    ip=round(e["entries"]/dt*100) if dt>0 else 0
    with col:
        st.markdown(f"""
        <div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);
            border-radius:14px;padding:16px;margin-bottom:10px">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
                <div style="width:40px;height:40px;border-radius:50%;background:rgba(99,102,241,.2);
                    border:1px solid rgba(99,102,241,.4);color:#A5B4FC;font-size:14px;font-weight:700;
                    display:flex;align-items:center;justify-content:center;flex-shrink:0">{e["initials"]}</div>
                <div style="flex:1">
                    <div style="display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin-bottom:3px">
                        <p style="font-weight:700;font-size:13px;margin:0;color:#F1F5F9">{e["name"]}</p>
                        <span class="wb-badge" style="background:{r_c}22;color:{r_c}">
                            <span style="width:5px;height:5px;border-radius:50%;background:{r_c};
                                display:inline-block;margin-right:3px"></span>{e["risk"]}
                        </span>
                    </div>
                    <p style="font-size:11px;color:#64748B;margin:0">
                        {e["dept"]} · {e["entries"]} entries · {ip}% of dept</p>
                    <div style="background:rgba(255,255,255,.06);border-radius:99px;height:4px;margin-top:5px">
                        <div style="width:{ip}%;height:4px;background:{r_c};border-radius:99px"></div>
                    </div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        bc1,bc2=st.columns(2)
        with bc1:
            if st.button(f"📋 Request Handover",key=f"rh_{e['id']}"):
                st.success(f"Request sent to {e['name']}!")
        with bc2:
            if st.button(f"🔄 Transfer Session",key=f"ts_{e['id']}"):
                st.info(f"Session scheduled with {e['name']}!")
