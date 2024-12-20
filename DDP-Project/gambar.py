import requests
from PIL import Image, ImageTk
import tkinter as tk

# Fungsi untuk mendapatkan data cuaca
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_main = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        return weather_main, temp
    else:
        return None, None

# Fungsi untuk menampilkan gambar berdasarkan cuaca
def get_image(weather):
    weather_images = {
        "Clear": "clear_sky.jpg",      # Ganti dengan path gambar langit cerah
        "Clouds": "cloudy.jpg",       # Ganti dengan path gambar berawan
        "Rain": "rain.jpg",           # Ganti dengan path gambar hujan
        "Snow": "snow.jpg",           # Ganti dengan path gambar salju
        "Thunderstorm": "storm.jpg",  # Ganti dengan path gambar badai
    }
    return weather_images.get(weather, "default.jpg")  # Gambar default jika cuaca tidak dikenal

# Program utama
def main():
    # Konfigurasi
    city = "Jakarta"  # Ganti dengan kota yang diinginkan
    api_key = "your_api_key"  # Ganti dengan API key Anda
    
    # Mendapatkan data cuaca
    weather, temp = get_weather(city, api_key)
    
    if weather:
        print(f"Kota: {city}")
        print(f"Cuaca: {weather}")
        print(f"Suhu: {temp}°C")
        
        # Menampilkan gambar
        image_path = get_image(weather)
        root = tk.Tk()
        root.title(f"Cuaca di {city}")
        
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(root, image=photo)
        label.pack()
        
        root.mainloop()
    else:
        print("Gagal mendapatkan data cuaca. Periksa nama kota atau API key Anda.")

if _name_ == "_main_":
    main()