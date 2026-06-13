"""📢 Announcements — WorkBrain"""
import streamlit as st
from data import ANNOUNCEMENTS

st.markdown('<h1 style="font-family:Syne,sans-serif;font-weight:800">📢 Announcements</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#94A3B8;margin-bottom:18px">Internal communications · {len(ANNOUNCEMENTS)} active</p>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📋 View All", "➕ Post Announcement"])

TYPE_C = {"Compliance":"#EF4444","Policy":"#8B5CF6","Event":"#3B82F6","Training":"#10B981","IT":"#06B6D4","Safety":"#EF4444","HR":"#8B5CF6"}
PRIO_C = {"Urgent":"#EF4444","High":"#F59E0B","Normal":"#6366F1","Low":"#94A3B8"}

with tab1:
    f1, f2 = st.columns(2)
    with f1:
        tf = st.selectbox("Filter by Type", ["All","Compliance","Policy","Event","Training","IT","Safety"])
    with f2:
        pf = st.selectbox("Filter by Priority", ["All","Urgent","High","Normal","Low"])

    shown = [a for a in ANNOUNCEMENTS if (tf=="All" or a["type"]==tf) and (pf=="All" or a["priority"]==pf)]

    for a in shown:
        tc = TYPE_C.get(a["type"],"#6366F1")
        pc = PRIO_C.get(a["priority"],"#6366F1")
        rp = round(a["reads"]/50*100)
        border = "rgba(239,68,68,.35)" if a["priority"]=="Urgent" else "rgba(255,255,255,.09)"
        st.markdown(f"""
        <div style="background:rgba(255,255,255,.04);border:1px solid {border};
            border-radius:16px;padding:20px;margin-bottom:14px">
            <div style="display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap;align-items:center">
                <span class="wb-badge" style="background:{tc}22;color:{tc}">{a["type"]}</span>
                <span class="wb-badge" style="background:{pc}22;color:{pc}">{a["priority"]}</span>
                <span style="margin-left:auto;font-size:12px;color:#475569">{a["reads"]}/50 read · {a["date"]}</span>
            </div>
            <h3 style="font-family:'Syne',sans-serif;font-size:15px;font-weight:700;
                margin:0 0 8px;color:#F1F5F9">{a["title"]}</h3>
            <p style="font-size:13px;color:#94A3B8;line-height:1.6;margin:0 0 12px">{a["body"]}</p>
            <div style="display:flex;align-items:center;gap:10px">
                <div style="flex:1;background:rgba(255,255,255,.06);border-radius:99px;height:4px">
                    <div style="width:{rp}%;height:4px;background:#6366F1;border-radius:99px"></div>
                </div>
                <span style="font-size:11px;color:#475569;white-space:nowrap">{rp}% read</span>
            </div>
            <p style="font-size:12px;color:#475569;margin:8px 0 0">— {a["author"]}</p>
        </div>""", unsafe_allow_html=True)

with tab2:
    st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:16px;margin-bottom:14px">Post New Announcement</h3>', unsafe_allow_html=True)
    with st.form("ann_form", clear_on_submit=True):
        at = st.text_input("Title *", placeholder="E.g. Mandatory Training Deadline")
        ab = st.text_area("Body *", placeholder="Full announcement text…", height=110)
        ac1, ac2 = st.columns(2)
        with ac1:
            atype = st.selectbox("Type", ["Compliance","Policy","Event","Training","IT","Safety","HR"])
        with ac2:
            aprio = st.selectbox("Priority", ["Urgent","High","Normal","Low"], index=2)
        if st.form_submit_button("📤 Post Announcement", use_container_width=True):
            if not at or not ab:
                st.error("Title and body are required.")
            else:
                st.success(f"✅ '{at}' posted to all employees!")
