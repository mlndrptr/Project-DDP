import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(page_title="Tentang Kami", page_icon=":star:")

# Konten Halaman About Us
st.title("Tentang aplikasi ini")
st.markdown("""Sebuah website cuaca di Jabodetabek biasanya dirancang user-friendly dengan desain responsif agar mudah diakses dari berbagai perangkat seperti komputer, tablet, atau ponsel. Fitur-fitur utama yang sering disediakan.

Serta Website ini dibuat dengan tujuan memberikan informasi dan layanan Cuaca secara real-time terkait kawasan Jabodetabek (Jakarta, Bogor, Depok, Tangerang, dan Bekasi). Situs ini dapat melayani berbagai kebutuhan pengguna, mulai dari informasi umum hingga rekomdasi yang kita perlukan
""")

st.header("Our Team!", divider="red")

# CSS untuk membuat konten rata tengah
st.markdown("""
<style>
.centered {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Data tim
tim = [
    {"nama": "Mulandari Putri", "nim": "0110124132 ", "kelompok": "(Ketua)", "image": "./images/mulan.jpeg"},
    {"nama": "Helma Hafiza Aulia", "nim": "0110124028", "kelompok": "(Anggota)", "image": "./images/helma.jpeg"},
    {"nama": "Izzah Himmatul Ashfiya", "nim": "0110124175", "kelompok": "(Anggota)", "image": "./images/izzah.jpeg"},
    {"nama": "Saskia Ramadani", "nim": "0110124114", "kelompok": "(Anggota)", "image": "./images/saskia.jpeg"}
]

# Membuat dua kolom
col1, col2 = st.columns(2)

# Iterasi melalui data tim
for i, member in enumerate(tim):
    # Menentukan kolom untuk setiap anggota
    current_col = col1 if i % 2 == 0 else col2
    
    with current_col:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.image(member["image"], width=150)
        st.markdown(f"<p>{member['nama']} - {member['nim']} {member['kelompok']}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Menambahkan pemisah setelah setiap dua anggota
    if i % 2 == 1 and i < len(tim) - 1:
        st.markdown("<hr/>", unsafe_allow_html=True)
