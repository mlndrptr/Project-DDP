import streamlit as st
import requests

# Halaman utama
st.header("Cuaca Wilayah Jabodetabek 🌦️🌡️", divider=True)
st.markdown("**Selamat datang di aplikasi cuaca Jabodetabek! Silakan pilih lokasi dan cek informasi cuaca.**", unsafe_allow_html=True)
st.image("./images/weather.png", caption="")

main = st.Page("./fitur/main.py", title="Weather")

pg = st.navigation(
    {
     "Menu Utama" : [main],
    }
)

pg.run()