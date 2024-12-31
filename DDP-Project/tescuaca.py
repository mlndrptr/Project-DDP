import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Halaman utama
st.set_page_config(page_title="Cuaca", page_icon="🌦️")
st.header("**Cuaca Wilayah Jabodetabek 🌦️🌡️**", divider=True)
st.markdown("**Selamat datang di aplikasi cuaca Jabodetabek! Silakan pilih lokasi dan cek informasi cuaca.**", unsafe_allow_html=True)
st.image("./images/weather.png", caption="")

# Fungsi untuk mendapatkan data cuaca
def get_weather_data(location):
    api_key = "cfd9a0d39ee02d75246d54a0442eb015"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric&lang=id"
    response = requests.get(url)
    return response.json()

# Fungsi untuk mendapatkan perkiraan cuaca per jam
def get_hourly_forecast(location):
    api_key = "cfd9a0d39ee02d75246d54a0442eb015"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric&lang=id"
    response = requests.get(url)
    return response.json()

# Sidebar untuk memilih lokasi
st.sidebar.header("Cek Lokasi Wilayah")
location = st.sidebar.selectbox("Pilih wilayah:", ["Jakarta", "Bogor", "Depok", "Tangerang", "Bekasi"])

# Variabel untuk menyimpan data cuaca
weather_data = None

st.sidebar.header("Cek Suhu & Cuaca")

# Menambahkan tanggal dan waktu saat ini
current_time = datetime.now()
st.markdown(f"Tanggal dan waktu saat ini: {current_time.strftime('%d-%m-%Y')} Waktu {current_time.strftime('%H:%M:%S')} WIB")

# Sidebar untuk cek suhu
if st.sidebar.button("Cek Suhu"):
    weather_data = get_weather_data(location)
    if weather_data.get("main"):
        temperature = weather_data["main"]["temp"]
        st.write(f"Suhu di {location} saat ini {temperature}°C")
    else:
        st.write("Data cuaca tidak ditemukan.")

# Sidebar untuk cek cuaca
if st.sidebar.button("Cek Cuaca"):
    if weather_data is None:
        weather_data = get_weather_data(location)
    if weather_data.get("weather"):
        weather_condition = weather_data["weather"][0]["description"]
        st.write(f"Kondisi cuaca di {location} saat ini {weather_condition}")
    else:
        st.write("Data cuaca tidak ditemukan.")

# Tampilan rekomendasi
if weather_data is not None and weather_data.get("weather"):
    if "hujan" in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: Sediakan payung atau jas hujan saat keluar.")
    elif "langit cerah" in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: Cuaca Cerah!")
    elif "cerah" in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: Cuaca cerah! Gunakan pakaian ringan dan jangan lupa sunscreen.")
    elif "mendung" in weather_data["weather"][0]["description"]:
        st.write ("Rekomendasi: Cuaca mendung, Anda mungkin memerlukan jaket ringan.")
    elif "badai petir" in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: Hati-hati dengan petir dan hujan lebat, sebaiknya tetap di dalam ruangan.")
    elif "cerah berawan" in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: cuaca pas digunakan untuk jalan santai.")
    else:
        st.write ("Rekomendasi: Cuaca normal. Nikmati hari Anda!")
else:
    st.write(" Silakan pilih wilayah terlebih dahulu, kemudian cek suhu atau cuaca untuk lebih detail !") 

# Sidebar untuk prediksi cuaca
st.sidebar.header("Prediksi Cuaca")
if st.sidebar.button("Prediksi Cuaca"):
    hourly_forecast = get_hourly_forecast(location)
    if hourly_forecast.get("list"):
        st.write(f"Perkiraan cuaca per 3 jam untuk wilayah {location} :")
        
        # Membuat list untuk menyimpan data
        data = []
        
        for index, hour in enumerate(hourly_forecast["list"]):
            if index >= 8:  # Menampilkan hingga 8 jam ke depan
                break
            time = hour["dt_txt"]
            temp = hour["main"]["temp"]
            weather_desc = hour["weather"][0]["description"]
            data.append({"Waktu": time, "Suhu (°C)": temp, "Kondisi": weather_desc})
        
        # Membuat DataFrame dari data
        df = pd.DataFrame(data)
        
        # Menampilkan DataFrame sebagai tabel tanpa indeks
        st.dataframe(df, hide_index=True)
    else:
        st.write("Data perkiraan cuaca tidak ditemukan.")