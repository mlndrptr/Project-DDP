import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(page_title="Tentang Kami", page_icon=":star:")

# Konten Halaman About Us
st.title("Tentang aplikasi ini")
st.markdown("""
Kami adalah tim yang berdedikasi untuk menyediakan solusi inovatif di bidang teknologi.
Kami percaya bahwa teknologi dapat mengubah dunia menjadi tempat yang lebih baik.
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
team_data = [
    {"name": "Mulandari Putri", "id": "0110124132", "image": "./images/mulan.jpeg"},
    {"name": "Helma Hafiza Aulia", "id": "0110124028", "image": "./images/helma.jpeg"},
    {"name": "Izzah Himmatul Ashfiya", "id": "0110124175", "image": "./images/izzah.jpeg"},
    {"name": "Saskia Ramadani", "id": "0110124114", "image": "./images/saskia.jpeg"}
]

# Membuat dua kolom
col1, col2 = st.columns(2)

# Iterasi melalui data tim
for i, member in enumerate(team_data):
    # Menentukan kolom untuk setiap anggota
    current_col = col1 if i % 2 == 0 else col2
    
    with current_col:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.image(member["image"], width=150)
        st.markdown(f"<p>{member['name']} - {member['id']}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Menambahkan pemisah setelah setiap dua anggota
    if i % 2 == 1 and i < len(team_data) - 1:
        st.markdown("<hr/>", unsafe_allow_html=True)