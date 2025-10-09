import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk


# ---------------------- Utility Functions ---------------------- #

def wind_degree_to_direction(degree):
    directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
    ]
    idx = int((degree / 22.5) + 0.5) % 16
    return directions[idx]


def unix_timestamp_to_localtime(timestamp, timezone_offset):
    local_time = datetime.utcfromtimestamp(timestamp + timezone_offset)
    return local_time.strftime("%I:%M %p")


def convert_temperature(kelvin, unit):
    if unit.upper() == "C":
        return f"{kelvin - 273.15:.2f} °C"
    elif unit.upper() == "F":
        return f"{(kelvin - 273.15) * 9/5 + 32:.2f} °F"
    else:
        return f"{kelvin:.2f} K"


# ---------------------- Core Functions ---------------------- #

def fetch_weather(api_key, location):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data:\n{e}")
        return None


def write_to_file(weather_data, temperature_unit):
    try:
        with open("weatherinfo.txt", "w+") as f:
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
            name = weather_data.get("name", "Unknown City")
            country = weather_data.get("sys", {}).get("country", "")
            f.write(f"Weather Stats for - {name}, {country} | {date_time}\n")
            f.write("-" * 60 + "\n")
            f.write(
                f"Temperature     : {convert_temperature(weather_data['main']['temp'], temperature_unit)}\n"
            )
            f.write(f"Description     : {weather_data['weather'][0]['description']}\n")
            f.write(f"Humidity        : {weather_data['main']['humidity']}%\n")
            f.write(f"Wind Speed      : {weather_data['wind']['speed']} km/h\n")
            f.write(
                f"Wind Direction  : {wind_degree_to_direction(weather_data['wind']['deg'])}\n"
            )
            f.write(
                f"Sunrise         : {unix_timestamp_to_localtime(weather_data['sys']['sunrise'], weather_data['timezone'])}\n"
            )
            f.write(
                f"Sunset          : {unix_timestamp_to_localtime(weather_data['sys']['sunset'], weather_data['timezone'])}\n"
            )
        messagebox.showinfo("Success", "Weather information saved to weatherinfo.txt")
    except IOError as e:
        messagebox.showerror("File Error", f"Error writing to file:\n{e}")


# ---------------------- GUI Application ---------------------- #

def get_weather():
    api_key = api_entry.get().strip()
    location = location_entry.get().strip()
    temp_unit = unit_choice.get().upper()

    if not api_key or not location:
        messagebox.showwarning("Input Error", "Please enter both API key and city name.")
        return

    weather_data = fetch_weather(api_key, location)
    if not weather_data:
        return

    if str(weather_data.get("cod")) == "401":
        messagebox.showerror("Invalid API Key", "Your API key is invalid.")
        return

    if str(weather_data.get("cod")) == "404":
        messagebox.showerror("City Not Found", "Please enter a valid city name.")
        return

    try:
        # Update GUI fields
        city_label.config(
            text=f"{weather_data['name']}, {weather_data['sys']['country']}"
        )
        temp_label.config(
            text=f"🌡 {convert_temperature(weather_data['main']['temp'], temp_unit)}"
        )
        desc_label.config(text=f"☁ {weather_data['weather'][0]['description'].capitalize()}")
        humidity_label.config(text=f"💧 Humidity: {weather_data['main']['humidity']}%")
        wind_label.config(
            text=f"💨 Wind: {weather_data['wind']['speed']} km/h ({wind_degree_to_direction(weather_data['wind']['deg'])})"
        )
        sunrise_label.config(
            text=f"🌅 Sunrise: {unix_timestamp_to_localtime(weather_data['sys']['sunrise'], weather_data['timezone'])}"
        )
        sunset_label.config(
            text=f"🌇 Sunset: {unix_timestamp_to_localtime(weather_data['sys']['sunset'], weather_data['timezone'])}"
        )

        write_to_file(weather_data, temp_unit)

    except KeyError:
        messagebox.showerror("Data Error", "Unexpected response structure from API.")


# ---------------------- GUI Layout ---------------------- #

root = tk.Tk()
root.title("🌦 Weather Information App")
root.geometry("480x500")
root.resizable(False, False)
root.configure(bg="#EAF6F6")

# Title
tk.Label(
    root,
    text="🌍 Weather Info App",
    font=("Segoe UI", 18, "bold"),
    bg="#EAF6F6",
    fg="#1A4D2E",
).pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#EAF6F6")
frame.pack(pady=10)

tk.Label(frame, text="API Key:", font=("Segoe UI", 10), bg="#EAF6F6").grid(row=0, column=0, padx=5, pady=5)
api_entry = tk.Entry(frame, width=40, show="*", relief="solid")
api_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="City:", font=("Segoe UI", 10), bg="#EAF6F6").grid(row=1, column=0, padx=5, pady=5)
location_entry = tk.Entry(frame, width=40, relief="solid")
location_entry.grid(row=1, column=1, padx=5)

tk.Label(frame, text="Unit:", font=("Segoe UI", 10), bg="#EAF6F6").grid(row=2, column=0, padx=5, pady=5)
unit_choice = ttk.Combobox(frame, values=["C", "F"], width=5, state="readonly")
unit_choice.grid(row=2, column=1, sticky="w", padx=5)
unit_choice.current(0)

# Fetch Button
tk.Button(
    root,
    text="Get Weather 🌦",
    command=get_weather,
    font=("Segoe UI", 11, "bold"),
    bg="#3B9AE1",
    fg="white",
    relief="ridge",
    padx=10,
    pady=5,
).pack(pady=10)

# Output Labels
output_frame = tk.Frame(root, bg="#EAF6F6")
output_frame.pack(pady=5)

city_label = tk.Label(output_frame, text="", font=("Segoe UI", 14, "bold"), bg="#EAF6F6")
city_label.pack(pady=5)

temp_label = tk.Label(output_frame, text="", font=("Segoe UI", 13), bg="#EAF6F6")
temp_label.pack(pady=5)

desc_label = tk.Label(output_frame, text="", font=("Segoe UI", 12, "italic"), bg="#EAF6F6")
desc_label.pack(pady=5)

humidity_label = tk.Label(output_frame, text="", font=("Segoe UI", 11), bg="#EAF6F6")
humidity_label.pack(pady=3)

wind_label = tk.Label(output_frame, text="", font=("Segoe UI", 11), bg="#EAF6F6")
wind_label.pack(pady=3)

sunrise_label = tk.Label(output_frame, text="", font=("Segoe UI", 11), bg="#EAF6F6")
sunrise_label.pack(pady=3)

sunset_label = tk.Label(output_frame, text="", font=("Segoe UI", 11), bg="#EAF6F6")
sunset_label.pack(pady=3)

# Footer
tk.Label(
    root,
    text="Data powered by OpenWeatherMap.org",
    font=("Segoe UI", 8),
    bg="#EAF6F6",
    fg="#666",
).pack(side="bottom", pady=10)

root.mainloop()
