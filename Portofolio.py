"""
Portofolio Muhammad Herlian - Python + Streamlit.

Menjalankan:
    pip install streamlit
    streamlit run Portofolio.py
"""
import html
import streamlit as st

# ======================= DATA (edit di sini) =======================
NAMA = "MUHAMMAD HERLIAN"
HEADLINE = "Informatics Engineering Student | Cybersecurity & Networking Enthusiast"
LOKASI = "Batam, Indonesia"
KONTAK = [
    ("✉️", "herlianmuhammad40@gmail.com", "mailto:herlianmuhammad40@gmail.com"),
    ("🔗", "LinkedIn", "https://www.linkedin.com/in/muhammad-herlian"),
    ("📸", "Instagram", "https://www.instagram.com/cak_iannn"),
]

TENTANG = (
    "Saya adalah mahasiswa semester 1 jurusan Teknik Informatika di Universitas Putra Batam "
    "dengan fokus peminatan pada Keamanan Siber (Cybersecurity) dan Jaringan Komputer "
    "(Computer Networking). Di samping aktivitas akademik dan pekerjaan, saya aktif menerapkan "
    "prinsip #LearnInPublic serta memanfaatkan kecerdasan buatan seperti Google Gemini sebagai "
    "tutor interaktif untuk mengakselerasi pemahaman logika pemrograman, arsitektur jaringan, "
    "dan analisis ancaman siber."
)

MATKUL = [
    ("Pengenalan Algoritma & Web",
     "Pemahaman logika alur program, struktur data dasar, serta fondasi pemodelan halaman web dasar (HTML/CSS)."),
    ("Matematika Diskrit & Kalkulus",
     "Logika matematika, teori himpunan, graf, dan fungsi yang menjadi dasar algoritma jaringan serta kriptografi di Cybersecurity."),
    ("Interaksi Manusia & Komputer (IMK)",
     "Prinsip antarmuka pengguna (UI/UX) dan kemudahan penggunaan aplikasi (usability)."),
    ("Inferensial Statistik & Komputer Aplikasi",
     "Analisis data dasar, pengolahan statistik untuk inferensi data, dan efisiensi penggunaan perangkat lunak komputer."),
]
TARGET = "Cybersecurity & Computer Networking"

TOOLS = [
    ("AI Acceleration", "Google Gemini (tutor interaktif untuk membedah logika Matematika Diskrit, Kalkulus, & Algoritma)"),
    ("Environment", "Visual Studio Code, Browser Developer Tools, Notion, LinkedIn"),
]

# (judul, kategori, deskripsi, hasil)
PROYEK = [
    ("Studi Interaktif Logika & Algoritma dengan Google Gemini", "AI Integration for Academic Study",
     "Memanfaatkan Google Gemini untuk mensimulasikan studi kasus logika Matematika Diskrit dan pemecahan masalah algoritma koding secara interaktif.",
     "Mempercepat pemahaman logika matematika dasar dan struktur algoritma tanpa mengurangi kedalaman pemahaman materi kuliah."),
    ("Eksperimen Pengembangan Web & Desain Antarmuka", "Web Development & IMK",
     "Latihan mandiri membangun struktur halaman web dasar dan menerapkan prinsip-prinsip Interaksi Manusia dan Komputer (IMK) agar antarmuka aplikasi ramah pengguna.",
     ""),
    ("Jurnal Belajar #LearnInPublic di LinkedIn", "Content Creation & Tech Sharing",
     "Merekam dan membagikan rangkuman pembelajaran mingguan seputar perkuliahan Teknik Informatika Universitas Putra Batam ke jaringan profesional LinkedIn.",
     ""),
]

PENDIDIKAN = {
    "gelar": "S1 Teknik Informatika",
    "kampus": "Universitas Putra Batam",
    "periode": "2026 - Sekarang (Mahasiswa Aktif)",
    "detail": [
        ("Peminatan target", "Cybersecurity & Computer Networking"),
        ("Status", "Semester 1 (Pekerja & Kuliah Malam)"),
    ],
}
# ===================================================================

e = html.escape
st.set_page_config(page_title=f"{NAMA.title()} | Portofolio", page_icon="🛰️", layout="centered")

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700;800&family=Instrument+Sans:wght@400;500;600&display=swap');
:root{--ink:#0F1B2D;--panel:#16263D;--line:#2A3F5C;--text:#E8EEF5;--mute:#93A4BC;--signal:#FFB547;--cyan:#5BC0EB;}
html,body,[class*="css"],.stApp{font-family:'Instrument Sans',sans-serif;color:var(--text);}
.stApp{background:var(--ink);}
header[data-testid="stHeader"],footer,#MainMenu{visibility:hidden;height:0;}
.block-container{max-width:760px;padding-top:2.5rem;padding-bottom:4rem;}
h1,h2,h3{font-family:'Bricolage Grotesque',sans-serif!important;color:var(--text)!important;letter-spacing:-0.02em;}
.hero h1{font-size:clamp(2.2rem,8vw,4rem);font-weight:800;line-height:1;margin:0 0 .6rem;}
.hero p{color:var(--mute);font-size:1.05rem;margin:.15rem 0;}
.links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;}
.links a{border:1px solid var(--line);border-radius:99px;padding:.3rem .9rem;text-decoration:none;font-size:.92rem;}
.links a:hover{border-color:var(--signal);}
.trace{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:1rem 1.2rem;margin:1.8rem 0 .5rem;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.85rem;overflow-x:auto;}
.trace .cmd{color:var(--mute);margin-bottom:.4rem;}
.hop{display:flex;gap:1rem;padding:.28rem 0;white-space:nowrap;}
.hop .n{color:var(--mute);width:1.4rem;text-align:right;}
.hop .h{color:var(--cyan);}
.hop.last .h{color:var(--signal);}
h2{font-size:1.6rem!important;margin-top:3rem!important;border-bottom:1px solid var(--line);padding-bottom:.4rem;}
.item{border-left:3px solid var(--cyan);background:var(--panel);padding:.8rem 1.1rem;margin:.7rem 0;border-radius:0 8px 8px 0;}
.item b{font-family:'Bricolage Grotesque',sans-serif;font-size:1.08rem;}
.item p{color:var(--mute);margin:.3rem 0 0;}
.proj{border-left-color:var(--signal);}
.proj .res{color:var(--text);margin-top:.5rem;}
.tag{display:inline-block;border:1px solid var(--cyan);color:var(--cyan);border-radius:99px;padding:.05rem .65rem;font-size:.78rem;margin-top:.4rem;}
.kv{display:flex;gap:.6rem;margin:.25rem 0;color:var(--mute);}
.kv span:first-child{min-width:9rem;}
.kv span:last-child{color:var(--text);}
a{color:var(--signal)!important;}
@media (prefers-reduced-motion:no-preference){.hero{animation:in .7s ease-out}@keyframes in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}}
</style>
""",
    unsafe_allow_html=True,
)

# ---- Hero ----
links = "".join(f'<a href="{u}" target="_blank">{i} {e(t)}</a>' for i, t, u in KONTAK)
hops = [m[0] for m in MATKUL] + [TARGET]
hop_html = "".join(
    f'<div class="hop{" last" if n == len(hops) else ""}"><span class="n">{n}</span><span class="h">{e(h)}</span></div>'
    for n, h in enumerate(hops, start=1)
)
st.markdown(
    f"""
<div class="hero">
  <h1>{e(NAMA)}</h1>
  <p>{e(HEADLINE)}</p>
  <p>📍 {e(LOKASI)}</p>
  <div class="links">{links}</div>
  <div class="trace"><div class="cmd">$ traceroute {e(TARGET.lower().replace(" ", "-"))}</div>{hop_html}</div>
</div>
""",
    unsafe_allow_html=True,
)

# ---- Tentang Saya ----
st.markdown("## Tentang Saya")
st.write(TENTANG)

# ---- Mata Kuliah ----
st.markdown("## Mata Kuliah & Fokus Pembelajaran Semester 1")
for judul, desk in MATKUL:
    st.markdown(f'<div class="item"><b>{e(judul)}</b><p>{e(desk)}</p></div>', unsafe_allow_html=True)

# ---- Tools ----
st.markdown("## Tools & Workspace")
for k, v in TOOLS:
    st.markdown(f'<div class="kv"><span>{e(k)}</span><span>{e(v)}</span></div>', unsafe_allow_html=True)

# ---- Proyek ----
st.markdown("## Proyek & Jurnal Belajar Semester 1")
for judul, kat, desk, hasil in PROYEK:
    res = f'<p class="res"><b>Hasil:</b> {e(hasil)}</p>' if hasil else ""
    st.markdown(
        f'<div class="item proj"><b>{e(judul)}</b><p>{e(desk)}</p>{res}<span class="tag">{e(kat)}</span></div>',
        unsafe_allow_html=True,
    )

# ---- Pendidikan ----
st.markdown("## Pendidikan")
detail = "".join(f'<div class="kv"><span>{e(k)}</span><span>{e(v)}</span></div>' for k, v in PENDIDIKAN["detail"])
st.markdown(
    f'<div class="item"><b>{e(PENDIDIKAN["gelar"])}, {e(PENDIDIKAN["kampus"])}</b>'
    f'<p>{e(PENDIDIKAN["periode"])}</p>{detail}</div>',
    unsafe_allow_html=True,
)