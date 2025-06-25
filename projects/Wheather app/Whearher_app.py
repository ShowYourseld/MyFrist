import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = '2452ea7fca95b6176cac6c5f9cd0c901'  # <-- Replace this!
    if not city:
        messagebox.showinfo("Info", "Please enter a city name.")
        return
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            city_name = data['name']
            result = (
                f"Weather in {city_name}:\n"
                f"Condition: {weather}\n"
                f"Temperature: {temperature}°C\n"
                f"Feels Like: {feels_like}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
        else:
            result = "Sorry, couldn't get weather for that city."
    except Exception as e:
        result = f"Error: {e}"
    weather_text.config(state='normal')
    weather_text.delete(1.0, tk.END)
    weather_text.insert(tk.END, result)
    weather_text.config(state='disabled')
    
def clear_fields():
    city_entry.delete(0, tk.END)
    weather_text.config(state='normal')
    weather_text.delete(1.0, tk.END)
    weather_text.config(state='disabled')

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

city_label = tk.Label(frame, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(frame, width=30)
city_entry.pack(pady=5)

clear_btm = tk.Button(frame, text="clear", command=clear_fields)
clear_btm.pack(pady=5)

get_btn = tk.Button(frame, text="Get Weather", command=get_weather)
get_btn.pack(pady=5)

weather_text = tk.Text(frame, width=40, height=10, state='disabled')
weather_text.pack(pady=10)

root.mainloop()