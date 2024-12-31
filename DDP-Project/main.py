import streamlit as st

aboutus = st.Page("./fitur/aboutus.py",  title="Tentang Kami", icon=":material/info:")
cuaca = st.Page("./fitur/cuaca.py", title="Cuaca", icon=":material/cloud:")

pg = st.navigation(
    {
     "" : [aboutus],
     "Menu Utama" : [cuaca],
    }
)

pg.run()

