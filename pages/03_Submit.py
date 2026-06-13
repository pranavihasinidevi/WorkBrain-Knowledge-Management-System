"""📝 Submit Knowledge — WorkBrain"""
import streamlit as st
from data import DEPARTMENTS, DEPT_COLORS

st.markdown('<h1 style="font-family:Syne,sans-serif;font-weight:800">📝 Submit Knowledge</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#94A3B8;margin-bottom:20px">Capture knowledge before it walks out the door — text form or voice upload.</p>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📝 Text Entry", "🎙️ Voice Upload"])

with tab1:
    with st.form("kb_form", clear_on_submit=True):
        st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:16px;margin-bottom:14px">Knowledge Entry Details</h3>', unsafe_allow_html=True)
        title = st.text_input("Title *", placeholder="E.g. Fix payment gateway 502 timeout error")
        c1, c2 = st.columns(2)
        with c1:
            dept = st.selectbox("Department *", ["Select…"] + DEPARTMENTS)
        with c2:
            priority = st.selectbox("Priority", ["Critical","High","Medium","Low"], index=2)
        c3, c4 = st.columns(2)
        with c3:
            etype = st.selectbox("Type", ["Problem/Solution","Lesson Learned","Best Practice","SOP Reference"])
        with c4:
            tags = st.text_input("Tags (comma separated)", placeholder="kubernetes, memory, devops")
        problem  = st.text_area("Problem Description *", placeholder="Describe the problem or situation clearly…", height=100)
        solution = st.text_area("Solution / How You Fixed It *", placeholder="Step-by-step how you resolved it…", height=100)
        submitted = st.form_submit_button("💾 Save Knowledge Entry", use_container_width=True)
        if submitted:
            if not title or dept == "Select…" or not problem or not solution:
                st.error("Please fill in Title, Department, Problem, and Solution.")
            else:
                st.success(f"✅ Entry **'{title}'** saved! It will appear in the Knowledge Base after review.")
                st.balloons()

with tab2:
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);
            border-radius:14px;padding:28px;text-align:center;margin-bottom:16px">
            <div style="font-size:52px;margin-bottom:12px">🎙️</div>
            <p style="font-size:14px;font-weight:600;color:#F1F5F9;margin:0 0 6px">Upload Voice Recording</p>
            <p style="font-size:12px;color:#64748B">Supports .mp3 .wav .m4a .ogg · max 30 seconds</p>
        </div>""", unsafe_allow_html=True)
        audio_file = st.file_uploader("Upload audio file", type=["mp3","wav","m4a","ogg"], label_visibility="collapsed")
        if audio_file:
            st.audio(audio_file)
            st.success("✅ Audio uploaded! Fill details below to create the entry.")
    with col2:
        st.markdown('<p style="font-size:12px;font-weight:600;color:#94A3B8;margin-bottom:8px">Recording History</p>', unsafe_allow_html=True)
        for t, d, dur, dt, status in [
            ("Fix payment timeout edge case","Engineering","0:28","2024-03-19","✅ Transcribed"),
            ("GST portal March workaround",  "Finance",    "0:30","2024-03-17","⏳ Pending"),
            ("HVAC noise fix procedure",     "Maintenance","0:22","2024-03-15","✅ Transcribed"),
        ]:
            dc = DEPT_COLORS.get(d,"#6366F1")
            st.markdown(f"""
            <div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);
                border-radius:10px;padding:11px;margin-bottom:8px">
                <p style="font-size:12px;font-weight:600;margin:0;color:#F1F5F9;
                    overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{t}</p>
                <div style="display:flex;gap:6px;margin-top:3px;align-items:center">
                    <span class="wb-badge" style="background:{dc}22;color:{dc}">{d}</span>
                    <span style="font-size:10px;color:#475569">⏱ {dur} · {dt}</span>
                    <span style="font-size:10px;color:{'#6EE7B7' if 'Trans' in status else '#FCD34D'};margin-left:auto">{status}</span>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")
    with st.form("voice_form", clear_on_submit=True):
        vc1, vc2 = st.columns(2)
        with vc1:
            vt = st.text_input("Title *", placeholder="What is this recording about?")
            vd = st.selectbox("Department", ["Select…"]+DEPARTMENTS, key="vd")
        with vc2:
            vp = st.selectbox("Priority", ["Critical","High","Medium","Low"], index=2, key="vp")
            vtags = st.text_input("Tags", placeholder="hvac, maintenance, repair")
        vsub = st.form_submit_button("💾 Save Voice Entry", use_container_width=True)
        if vsub:
            if vt and vd != "Select…":
                st.success(f"✅ Voice entry '{vt}' saved and queued for transcription!")
            else:
                st.error("Please fill Title and Department.")
