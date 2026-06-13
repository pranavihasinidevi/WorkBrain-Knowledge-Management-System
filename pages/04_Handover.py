"""🔄 Handover Docs — WorkBrain"""
import streamlit as st
from data import HANDOVERS, DEPARTMENTS, DEPT_COLORS

st.markdown('<h1 style="font-family:Syne,sans-serif;font-weight:800">🔄 Handover Documentation</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#94A3B8;margin-bottom:18px">Capture institutional knowledge before employees exit.</p>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📋 View Handovers", "➕ New Handover"])

STATUS_C = {"Approved":"#10B981","Pending Approval":"#F59E0B","Draft":"#6366F1","Rejected":"#EF4444"}

with tab1:
    for h in HANDOVERS:
        dc   = DEPT_COLORS.get(h["dept"], "#6366F1")
        sc   = STATUS_C.get(h["status"], "#6366F1")
        pc_c = "#10B981" if h["completion"]==100 else ("#F59E0B" if h["completion"]>=60 else "#EF4444")
        label = f'{h["employee"]} · {h["dept"]} · {h["status"]}  ({h["completion"]}% complete)'

        with st.expander(label):
            left, right = st.columns([2.5, 1])
            with left:
                st.markdown(f"""
                <div style="display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap">
                    <span class="wb-badge" style="background:{dc}22;color:{dc}">{h["dept"]}</span>
                    <span class="wb-badge" style="background:{sc}22;color:{sc}">{h["status"]}</span>
                </div>
                <p style="font-size:13px;color:#94A3B8;margin-bottom:14px">
                    <strong style="color:#F1F5F9">{h["role"]}</strong> &nbsp;·&nbsp;
                    Last day: <strong style="color:#F1F5F9">{h["lastDay"]}</strong> &nbsp;·&nbsp;
                    Manager: <strong style="color:#F1F5F9">{h["manager"]}</strong>
                </p>""", unsafe_allow_html=True)

                st.markdown(f"**Completion: {h['completion']}%**")
                st.progress(h["completion"] / 100)
                st.markdown("<br>", unsafe_allow_html=True)

                for icon, lbl, val in [
                    ("📋","Responsibilities", h["responsibilities"]),
                    ("🗂️","Current Projects",  h["projects"]),
                    ("⏳","Pending Tasks",     h["pending"]),
                    ("👥","Key Contacts",      h["contacts"]),
                    ("💡","Lessons Learned",   h["lessons"]),
                    ("🚀","Recommendations",   h["recommendations"]),
                ]:
                    st.markdown(f"""
                    <div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);
                        border-radius:10px;padding:12px 14px;margin-bottom:8px">
                        <p style="font-size:10px;font-weight:700;color:#475569;text-transform:uppercase;
                            letter-spacing:.5px;margin:0 0 4px">{icon} {lbl}</p>
                        <p style="font-size:13px;color:#CBD5E1;margin:0;line-height:1.6">{val}</p>
                    </div>""", unsafe_allow_html=True)

            with right:
                st.markdown(f"""
                <div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);
                    border-radius:14px;padding:18px;text-align:center">
                    <div style="width:52px;height:52px;border-radius:50%;background:rgba(99,102,241,.2);
                        border:1px solid rgba(99,102,241,.4);color:#A5B4FC;font-size:18px;font-weight:700;
                        display:flex;align-items:center;justify-content:center;margin:0 auto 10px">
                        {h["initials"]}</div>
                    <p style="font-size:14px;font-weight:700;color:#F1F5F9;margin:0">{h["employee"]}</p>
                    <p style="font-size:12px;color:#64748B;margin:3px 0">{h["role"]}</p>
                </div>""", unsafe_allow_html=True)

                if h["status"] == "Pending Approval":
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("✅ Approve", key=f"ap_{h['id']}", use_container_width=True):
                        st.success(f"Handover for {h['employee']} approved!")
                    if st.button("❌ Reject", key=f"rj_{h['id']}", use_container_width=True):
                        st.warning("Handover rejected. Employee notified.")

with tab2:
    st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:16px;margin-bottom:14px">Submit New Handover</h3>', unsafe_allow_html=True)
    with st.form("handover_form", clear_on_submit=True):
        hc1, hc2 = st.columns(2)
        with hc1:
            h_name = st.text_input("Employee Name *")
            h_dept = st.selectbox("Department *", ["Select…"] + DEPARTMENTS)
        with hc2:
            h_role = st.text_input("Job Role *")
            h_last = st.date_input("Last Working Day *")
        for lbl, ph in [
            ("📋 Responsibilities", "Primary responsibilities…"),
            ("🗂️ Current Projects",  "Projects and their status…"),
            ("⏳ Pending Tasks",     "Unresolved tasks or open items…"),
            ("👥 Key Contacts",      "Who successor should contact…"),
            ("💡 Lessons Learned",   "What you wish you knew on Day 1…"),
            ("🚀 Recommendations",   "Advice for your successor…"),
        ]:
            st.text_area(lbl, placeholder=ph, height=80)
        hs1, hs2 = st.columns(2)
        with hs1:
            if st.form_submit_button("📤 Submit for Approval", use_container_width=True):
                if not h_name or h_dept == "Select…" or not h_role:
                    st.error("Name, Department, and Role are required.")
                else:
                    st.success(f"✅ Handover for {h_name} submitted!")
        with hs2:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("Draft saved.")
