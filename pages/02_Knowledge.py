"""🔍 Knowledge Base — WorkBrain"""
import streamlit as st
from data import KNOWLEDGE, DEPARTMENTS, DEPT_COLORS

st.markdown('<h1 style="font-family:Syne,sans-serif;font-weight:800">🔍 Knowledge Base</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#94A3B8;margin-bottom:18px">{len(KNOWLEDGE)} entries · Problems · Solutions · SOPs · Lessons Learned</p>', unsafe_allow_html=True)

# Filters
f1, f2, f3 = st.columns([3, 1.5, 1.5])
with f1:
    q = st.text_input("Search", placeholder="🔍  Search by title, tag, or author…", label_visibility="collapsed")
with f2:
    dept_f = st.selectbox("Dept", ["All Departments"] + DEPARTMENTS, label_visibility="collapsed")
with f3:
    prio_f = st.selectbox("Priority", ["All Priorities","Critical","High","Medium","Low"], label_visibility="collapsed")

filtered = KNOWLEDGE
if q:
    sq = q.lower()
    filtered = [k for k in filtered if sq in k["title"].lower() or sq in k["author"].lower() or sq in k["tags"].lower()]
if dept_f != "All Departments":
    filtered = [k for k in filtered if k["dept"] == dept_f]
if prio_f != "All Priorities":
    filtered = [k for k in filtered if k["priority"] == prio_f]

st.markdown(f'<p style="font-size:13px;color:#64748B;margin-bottom:4px">{len(filtered)} result(s)</p>', unsafe_allow_html=True)

if not filtered:
    st.info("🔍 No entries found. Try different search terms or clear the filters.")
else:
    for k in filtered:
        dc  = DEPT_COLORS.get(k["dept"], "#6366F1")
        pc  = {"Critical":"#EF4444","High":"#F59E0B","Medium":"#3B82F6","Low":"#10B981"}.get(k["priority"],"#6366F1")
        stars = "★" * round(k["rating"]) + "☆" * (5 - round(k["rating"]))
        label = f'{k["title"]}  ·  {k["dept"]}  ·  {k["priority"]}{"  ✅" if k["verified"] else ""}'

        with st.expander(label):
            left, right = st.columns([2.2, 1])
            with left:
                # Badges
                vbadge = '<span class="wb-badge" style="background:rgba(16,185,129,.15);color:#6EE7B7">✓ Manager Verified</span>' if k["verified"] else ""
                tags_html = "".join(f'<span class="wb-badge" style="background:rgba(255,255,255,.06);color:#64748B">#{t.strip()}</span>' for t in k["tags"].split(","))
                st.markdown(f"""
                <div style="display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap">
                    <span class="wb-badge" style="background:{dc}22;color:{dc}">{k["dept"]}</span>
                    <span class="wb-badge" style="background:{pc}22;color:{pc}">{k["priority"]}</span>
                    <span class="wb-badge" style="background:rgba(255,255,255,.07);color:#64748B">{k["type"]}</span>
                    {vbadge}
                </div>
                <div style="background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.2);
                    border-radius:10px;padding:14px;margin-bottom:10px">
                    <p style="font-size:11px;font-weight:700;color:#FCD34D;margin:0 0 6px;
                        text-transform:uppercase;letter-spacing:.8px">🔴 Problem</p>
                    <p style="font-size:13px;color:#CBD5E1;margin:0;line-height:1.7">{k["problem"]}</p>
                </div>
                <div style="background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.2);
                    border-radius:10px;padding:14px;margin-bottom:12px">
                    <p style="font-size:11px;font-weight:700;color:#6EE7B7;margin:0 0 6px;
                        text-transform:uppercase;letter-spacing:.8px">✅ Solution</p>
                    <p style="font-size:13px;color:#CBD5E1;margin:0;line-height:1.7">{k["solution"]}</p>
                </div>
                <div>{tags_html}</div>
                """, unsafe_allow_html=True)

            with right:
                st.markdown(f"""
                <div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);
                    border-radius:12px;padding:16px;margin-bottom:12px">
                    <p style="font-size:11px;color:#64748B;margin:0 0 6px">Author</p>
                    <p style="font-size:13px;font-weight:700;color:#F1F5F9;margin:0 0 10px">{k["author"]}</p>
                    <p style="font-size:11px;color:#64748B;margin:0 0 2px">📅 {k["date"]}</p>
                    <p style="font-size:13px;color:#F59E0B;margin:0 0 8px">{stars} {k["rating"]}</p>
                    <p style="font-size:11px;color:#64748B;margin:0">👁 {k["views"]} views</p>
                    <p style="font-size:11px;color:#64748B;margin:3px 0">💬 {k["comments"]} comments</p>
                    <p style="font-size:11px;color:#64748B;margin:0">👍 {k["helpful"]} helpful</p>
                </div>
                """, unsafe_allow_html=True)

            bc1, bc2, bc3 = st.columns(3)
            with bc1:
                if st.button("👍 Helpful", key=f"h_{k['id']}"):
                    st.success("Marked as helpful!")
            with bc2:
                if st.button("💬 Comment", key=f"c_{k['id']}"):
                    st.info("Comments require database integration.")
            with bc3:
                if st.button("✅ Verify", key=f"v_{k['id']}"):
                    st.success("Entry verified!")
