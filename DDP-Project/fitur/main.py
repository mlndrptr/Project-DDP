import streamlit as st
import requests

# Fungsi untuk mendapatkan data cuaca
def get_weather_data(location):
    api_key = "cfd9a0d39ee02d75246d54a0442eb015"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric&lang=id"
    response = requests.get(url)
    return response.json()

# Sidebar untuk memilih lokasi
st.sidebar.header("Cek Lokasi Wilayah")
location = st.sidebar.selectbox("Pilih wilayah:", ["Jakarta", "Bogor", "Depok", "Tangerang", "Bekasi"])

# Variabel untuk menyimpan data cuaca
weather_data = None

# Sidebar untuk cek suhu
st.sidebar.header("Cek Informasi Cuaca")
if st.sidebar.button("Cek Suhu"):
    weather_data = get_weather_data(location)
    if weather_data.get("main"):
        temperature = weather_data["main"]["temp"]
        st.write(f"Suhu di {location} adalah {temperature}°C")
    else:
        st.write("Data cuaca tidak ditemukan.")

# Sidebar untuk cek cuaca
#st.sidebar.header("Cek Cuaca")
if st.sidebar.button("Cek Cuaca"):
    if weather_data is None:
        weather_data = get_weather_data(location)
    if weather_data.get("weather"):
        weather_condition = weather_data["weather"][0]["description"]
        st.write(f"Kondisi cuaca di {location} adalah {weather_condition}")
    else:
        st.write("Data cuaca tidak ditemukan.")

# Sidebar untuk rekomendasi
st.sidebar.header("Rekomendasi")

if weather_data is not None and weather_data.get("weather"):
    if "hujan"in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: sediakan payung atau jas hujan saat keluar.")
    elif "langit cerah" in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: Cuaca Cerah!")
    elif "cerah" in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: Cuaca cerah! Gunakan pakaian ringan dan jangan lupa sunscreen.")
    elif "mendung" in weather_data["weather"][0]["description"]:
        st.write ("Rekomendasi: Cuaca mendung Anda mungkin memerlukan jaket ringan.")
    elif "badai petir"in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: Hati-hati dengan petir dan hujan lebat, sebaiknya tetap di dalam ruangan.")
    elif "cerah berawan"in weather_data["weather"][0]["description"]:
        st.write("Rekomendasi: cuaca pas digunakan untuk jalan santai.")
else:
    st.write("Silakan cek suhu atau cuaca terlebih dahulu.")