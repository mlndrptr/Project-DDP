import streamlit as st
import requests
from datetime import datetime

# Fungsi untuk mendapatkan data cuaca
def get_weather_data(location):
    api_key = "cfd9a0d39ee02d75246d54a0442eb015"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric&lang=id"
    response = requests.get(url)
    return response.json()

# Fungsi untuk mendapatkan data prediksi cuaca mingguan
def get_weekly_weather(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?id&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}

# Halaman utama
st.title("Aplikasi Cuaca Jabodetabek")
st.write("Selamat datang di aplikasi cuaca Jabodetabek! Silakan pilih lokasi dan cek informasi cuaca.")

# Sidebar untuk memilih lokasi
st.sidebar.header("Cek Lokasi Wilayah")
location = st.sidebar.selectbox("Pilih wilayah:", ["Jakarta", "Bogor", "Depok", "Tangerang", "Bekasi"])

# Koordinat untuk masing-masing wilayah
coords = {
    "Jakarta": {"lat": -6.2088, "lon": 106.8456},
    "Bogor": {"lat": -6.5950, "lon": 106.8166},
    "Depok": {"lat": -6.4025, "lon": 106.7942},
    "Tangerang": {"lat": -6.1783, "lon": 106.6319},
    "Bekasi": {"lat": -6.2383, "lon": 106.9756},
}

# Variabel untuk menyimpan data cuaca
weather_data = None

# Sidebar untuk cek suhu
st.sidebar.header("Cek Suhu")
if st.sidebar.button("Cek Suhu"):
    weather_data = get_weather_data(location)
    if weather_data.get("main"):
        temperature = weather_data["main"]["temp"]
        st.write(f"Suhu di {location} adalah {temperature} °C")
    else:
        st.write("Data cuaca tidak ditemukan.")

# Sidebar untuk cek cuaca
if st.sidebar.button("Cek Cuaca"):
    if weather_data is None:
        weather_data = get_weather_data(location)
    if weather_data.get("weather"):
        weather_condition = weather_data["weather"][0]["description"]
        st.write(f"Kondisi cuaca di {location} adalah {weather_condition}")
    else:
        st.write("Data cuaca tidak ditemukan.")

# Sidebar untuk prediksi cuaca mingguan
st.sidebar.header("Prediksi Cuaca Mingguan")
if st.sidebar.button("Lihat Prediksi Mingguan"):
    lat, lon = coords[location]["lat"], coords[location]["lon"]
    weekly_data = get_weekly_weather(lat, lon, api_key="cfd9a0d39ee02d75246d54a0442eb015")

    if "daily" in weekly_data:
        st.write(f"Prediksi Cuaca di {location} selama 7 hari ke depan:")
        for day in weekly_data["daily"]:
            dt = datetime.utcfromtimestamp(day["dt"]).strftime('%d-%m-%Y')
            temp = day["temp"]["day"]
            weather_desc = day["weather"][0]["description"]
            st.write(f"{dt}: {weather_desc}, suhu: {temp} °C")
    else:
        st.write("Data cuaca tidak ditemukan atau tidak lengkap.")

# Sidebar untuk rekomendasi
st.sidebar.header("Rekomendasi")

if "hujan"in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: sediakan payung atau jas hujan saat keluar.")
    elif "cerah" in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: Cuaca cerah! Gunakan pakaian ringan dan jangan lupa sunscreen.")
    elif "mendung" in weather_data["weather"][0]["description"]:
        st.write ("Rekomendasi: Cuaca mendung Anda mungkin memerlukan jaket ringan.")
    elif "badai petir"in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: Hati-hati dengan petir dan hujan lebat, sebaiknya tetap di dalam ruangan.")
   elif "cerah berawan"in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: cuaca pas digunakan untuk jalan santai.")
    else:
        st.write ("Rekomendasi: Cuaca normal. Nikmati hari Anda!")
