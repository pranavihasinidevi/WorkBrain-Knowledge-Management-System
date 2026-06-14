"""📱 QR Code Access — LegacyOS"""
import streamlit as st, qrcode, io
from data import QR_MACHINES, KNOWLEDGE, DEPARTMENTS, DEPT_COLORS

st.markdown('<h1 style="font-family:Syne,sans-serif;font-weight:800">📱 QR Code Knowledge Access</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#94A3B8;margin-bottom:18px">Scan any machine, system, or process to instantly surface its full knowledge history.</p>', unsafe_allow_html=True)

def gen_qr(data):
    qr=qrcode.QRCode(version=1,box_size=6,border=2,error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(data); qr.make(fit=True)
    img=qr.make_image(fill_color="#0B0F1A",back_color="white")
    buf=io.BytesIO(); img.save(buf,format="PNG"); buf.seek(0)
    return buf

tab1,tab2=st.tabs(["📱 QR Gallery","➕ Generate New QR"])

with tab1:
    df=st.selectbox("Filter by Department",["All"]+DEPARTMENTS)
    shown=[q for q in QR_MACHINES if df=="All" or q["dept"]==df]
    cols=st.columns(2)
    for i,q in enumerate(shown):
        col=cols[i%2]
        dc=DEPT_COLORS.get(q["dept"],"#6366F1")
        url=f"https://workbrain.app/knowledge/{q['code']}"
        buf=gen_qr(url)
        related=[k for k in KNOWLEDGE if k["dept"]==q["dept"]][:2]
        rel_html="".join(
            f'<div style="padding:8px 10px;border-radius:8px;background:rgba(255,255,255,.03);margin-bottom:5px">'
            f'<p style="font-size:11px;font-weight:600;color:#F1F5F9;margin:0">{k["title"]}</p>'
            f'<p style="font-size:10px;color:#475569;margin:2px 0 0">👁 {k["views"]} · {"✅ Verified" if k["verified"] else "Unverified"}</p>'
            f'</div>' for k in related)
        with col:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);
                border-radius:16px;padding:20px;margin-bottom:14px">
                <div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:14px">
                    <div style="flex:1">
                        <p style="font-size:24px;margin:0 0 4px">{q["icon"]}</p>
                        <p style="font-size:14px;font-weight:700;margin:0 0 6px;color:#F1F5F9">{q["name"]}</p>
                        <span class="wb-badge" style="background:{dc}22;color:{dc}">{q["dept"]}</span>
                        <div style="display:flex;gap:10px;margin-top:8px;font-size:12px;color:#64748B">
                            <span>📊 {q["scans"]} scans</span><span>📄 {q["type"]}</span>
                        </div>
                        <p style="font-size:9px;color:#334155;margin:6px 0 0;font-family:monospace">{q["code"]}</p>
                    </div>
                </div>
                <p style="font-size:10px;font-weight:700;color:#475569;text-transform:uppercase;
                    letter-spacing:.5px;margin-bottom:6px">Related Knowledge</p>
                {rel_html}
            </div>""", unsafe_allow_html=True)
            st.image(buf, width=140, caption=f"Scan → {q['code']}")
            buf2=gen_qr(url)
            st.download_button(f"⬇ Download QR",data=buf2,
                file_name=f"workbrain_{q['code']}.png",mime="image/png",key=f"dl_{q['id']}")
            st.markdown("<br>",unsafe_allow_html=True)

with tab2:
    st.markdown('<h3 style="font-family:Syne,sans-serif;font-size:16px;margin-bottom:14px">Generate New QR Code</h3>', unsafe_allow_html=True)
    with st.form("qr_form"):
        gc1,gc2=st.columns(2)
        with gc1:
            gn=st.text_input("Machine / System Name *",placeholder="E.g. Boiler Unit C-05")
            gd=st.selectbox("Department *",["Select…"]+DEPARTMENTS)
        with gc2:
            gt=st.selectbox("Type",["Machine","Software","Infrastructure","Process","Area"])
            st.text_input("Code (auto-assigned)","WB-NEW-001",disabled=True)
        if st.form_submit_button("🔲 Generate QR Code",use_container_width=True):
            if not gn or gd=="Select…":
                st.error("Name and Department required.")
            else:
                url2=f"https://workbrain.app/knowledge/WB-NEW-001"
                buf3=gen_qr(url2)
                st.success(f"✅ QR Code generated for **{gn}**!")
                st.image(buf3,width=200,caption=f"URL: {url2}")
                st.download_button("⬇ Download QR",data=buf3,
                    file_name="workbrain_new.png",mime="image/png")
