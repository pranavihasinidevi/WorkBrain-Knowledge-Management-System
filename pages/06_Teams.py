"""👥 Teams — WorkBrain"""
import streamlit as st
from data import EMPLOYEES, DEPARTMENTS, DEPT_COLORS

st.markdown('<h1 style="font-family:Syne,sans-serif;font-weight:800">👥 Team Directory</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#94A3B8;margin-bottom:18px">{len(EMPLOYEES)} employees · 6 departments</p>', unsafe_allow_html=True)

RISK_C = {"Critical":"#EF4444","High":"#F59E0B","Medium":"#6366F1","Low":"#10B981"}

f1, f2, f3 = st.columns([2,1.5,1.5])
with f1: sq = st.text_input("Search", placeholder="🔍  Name or role…", label_visibility="collapsed")
with f2: df = st.selectbox("Dept",  ["All"]+DEPARTMENTS, label_visibility="collapsed")
with f3: rf = st.selectbox("Risk",  ["All","Critical","High","Medium","Low"], label_visibility="collapsed")

filt = EMPLOYEES
if sq: filt=[e for e in filt if sq.lower() in e["name"].lower() or sq.lower() in e["role"].lower()]
if df!="All": filt=[e for e in filt if e["dept"]==df]
if rf!="All": filt=[e for e in filt if e["risk"]==rf]

# Summary
s1,s2,s3,s4=st.columns(4)
s1.metric("👥 Showing",    len(filt))
s2.metric("✅ Active",     len([e for e in filt if e["status"]=="Active"]))
s3.metric("🔴 Critical",   len([e for e in filt if e["risk"]=="Critical"]))
s4.metric("📚 Total Entries", sum(e["entries"] for e in filt))

st.markdown("---")

rows=[filt[i:i+3] for i in range(0,len(filt),3)]
for row in rows:
    cols=st.columns(3)
    for col, e in zip(cols, row):
        dc=DEPT_COLORS.get(e["dept"],"#6366F1")
        rc=RISK_C.get(e["risk"],"#10B981")
        sc="#10B981" if e["status"]=="Active" else "#EF4444"
        col.markdown(f"""
        <div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);
            border-radius:16px;padding:18px;margin-bottom:12px">
            <div style="display:flex;gap:10px;margin-bottom:12px">
                <div style="width:44px;height:44px;border-radius:50%;background:rgba(99,102,241,.2);
                    border:1px solid rgba(99,102,241,.4);color:#A5B4FC;font-size:16px;font-weight:700;
                    display:flex;align-items:center;justify-content:center;flex-shrink:0">{e["initials"]}</div>
                <div style="flex:1;min-width:0">
                    <p style="font-size:14px;font-weight:700;margin:0;color:#F1F5F9;
                        overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{e["name"]}</p>
                    <p style="font-size:11px;color:#64748B;margin:2px 0 4px">{e["role"]}</p>
                    <div>
                        <span class="wb-badge" style="background:{dc}22;color:{dc}">{e["dept"]}</span>
                        <span class="wb-badge" style="background:{sc}22;color:{sc}">{e["status"]}</span>
                    </div>
                </div>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:8px">
                <div style="text-align:center;padding:7px;background:rgba(255,255,255,.03);border-radius:8px">
                    <p style="font-size:17px;font-weight:800;color:#6366F1;margin:0">{e["entries"]}</p>
                    <p style="font-size:9px;color:#475569;margin:0">Entries</p>
                </div>
                <div style="text-align:center;padding:7px;background:rgba(255,255,255,.03);border-radius:8px">
                    <p style="font-size:17px;font-weight:800;color:#10B981;margin:0">{e["score"]}</p>
                    <p style="font-size:9px;color:#475569;margin:0">K-Score</p>
                </div>
                <div style="text-align:center;padding:7px;background:rgba(255,255,255,.03);border-radius:8px">
                    <p style="font-size:12px;font-weight:700;color:{rc};margin:0">{e["risk"]}</p>
                    <p style="font-size:9px;color:#475569;margin:0">Risk</p>
                </div>
            </div>
            <p style="font-size:11px;color:#475569;margin:0">📧 {e["email"]}</p>
        </div>""", unsafe_allow_html=True)
