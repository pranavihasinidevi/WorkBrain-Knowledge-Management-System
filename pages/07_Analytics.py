"""📈 Analytics — WorkBrain"""
import streamlit as st
import plotly.graph_objects as go
from data import KNOWLEDGE, EMPLOYEES, DEPARTMENTS, DEPT_COLORS

st.markdown('<h1 style="font-family:Syne,sans-serif;font-weight:800">📈 Analytics & Reporting</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#94A3B8;margin-bottom:18px">Knowledge health metrics across your organization.</p>', unsafe_allow_html=True)

verified=len([k for k in KNOWLEDGE if k["verified"]])

k1,k2,k3,k4=st.columns(4)
k1.metric("👁 Total Views","14.2K","↑ 18% this month")
k2.metric("📝 Contributions",len(KNOWLEDGE),"↑ 12 this month")
k3.metric("✅ Verified",verified,"manager approved")
k4.metric("👤 Active Users","13","of 15 employees")

st.markdown("---")

col1,col2=st.columns(2)

with col1:
    dc={d:len([k for k in KNOWLEDGE if k["dept"]==d]) for d in DEPARTMENTS}
    fig=go.Figure(go.Bar(x=list(dc.keys()),y=list(dc.values()),
        marker_color=[DEPT_COLORS[d] for d in dc],marker_line_width=0))
    fig.update_layout(
        title=dict(text="Department Contributions",font=dict(color="#F1F5F9",size=14,family="Inter")),
        paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94A3B8",family="Inter"),
        xaxis=dict(showgrid=False,tickfont=dict(color="#64748B")),
        yaxis=dict(showgrid=True,gridcolor="rgba(255,255,255,.06)",tickfont=dict(color="#64748B")),
        margin=dict(l=0,r=0,t=40,b=0),height=260)
    st.plotly_chart(fig,use_container_width=True)

with col2:
    topics=["kubernetes","GST","CRM","python","onboarding","security","docker","payroll"]
    counts=[89,67,61,55,48,41,35,31]
    fig2=go.Figure(go.Bar(y=topics,x=counts,orientation="h",
        marker_color=["#6366F1","#8B5CF6","#3B82F6","#10B981","#F59E0B","#EF4444","#06B6D4","#8B5CF6"],
        marker_line_width=0))
    fig2.update_layout(
        title=dict(text="🔥 Trending Topics",font=dict(color="#F1F5F9",size=14,family="Inter")),
        paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94A3B8",family="Inter"),
        xaxis=dict(showgrid=True,gridcolor="rgba(255,255,255,.06)",tickfont=dict(color="#64748B")),
        yaxis=dict(showgrid=False,tickfont=dict(color="#94A3B8")),
        margin=dict(l=0,r=0,t=40,b=0),height=260)
    st.plotly_chart(fig2,use_container_width=True)

vc1,vc2=st.columns(2)
with vc1:
    unv=len(KNOWLEDGE)-verified
    fig3=go.Figure(go.Pie(
        labels=["Verified","Unverified"],values=[verified,unv],hole=0.55,
        marker_colors=["#10B981","rgba(255,255,255,.08)"],
        textfont=dict(color="#F1F5F9")))
    fig3.update_layout(
        title=dict(text="Verification Rate",font=dict(color="#F1F5F9",size=14,family="Inter")),
        paper_bgcolor="rgba(0,0,0,0)",font=dict(color="#94A3B8"),
        legend=dict(font=dict(color="#94A3B8")),
        margin=dict(l=0,r=0,t=40,b=0),height=260)
    st.plotly_chart(fig3,use_container_width=True)

with vc2:
    st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:15px;margin-bottom:12px">🏆 Top Contributors</h3>', unsafe_allow_html=True)
    RANK_C=["#F59E0B","#94A3B8","#CD7F32"]
    for i,e in enumerate(sorted(EMPLOYEES,key=lambda x:x["entries"],reverse=True)[:8],1):
        dc2=DEPT_COLORS.get(e["dept"],"#6366F1")
        rc=RANK_C[i-1] if i<=3 else "#475569"
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;padding:9px;border-radius:10px;
            background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);margin-bottom:6px">
            <span style="font-size:13px;font-weight:800;color:{rc};width:20px">#{i}</span>
            <div style="width:32px;height:32px;border-radius:50%;background:rgba(99,102,241,.2);
                color:#A5B4FC;font-size:11px;font-weight:700;display:flex;align-items:center;
                justify-content:center">{e["initials"]}</div>
            <div style="flex:1">
                <p style="font-size:13px;font-weight:600;margin:0;color:#F1F5F9">{e["name"]}</p>
                <span class="wb-badge" style="background:{dc2}22;color:{dc2}">{e["dept"]}</span>
            </div>
            <div style="text-align:right">
                <p style="font-size:16px;font-weight:800;color:#6366F1;margin:0">{e["entries"]}</p>
                <p style="font-size:9px;color:#475569;margin:0">entries</p>
            </div>
        </div>""", unsafe_allow_html=True)
