import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your actual API key
API_KEY = "1ea564abe6c01a3a3def03c24db3b1c9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        weather_info = (
            f"City: {data['name']}, {data['sys']['country']}\n"
            f"Temperature: {data['main']['temp']} °C\n"
            f"Weather: {data['weather'][0]['description'].title()}\n"
            f"Humidity: {data['main']['humidity']} %\n"
            f"Wind Speed: {data['wind']['speed']} m/s"
        )
        result_label.config(text=weather_info)

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# --- UI Setup ---
root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)

city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

root.mainloop()
