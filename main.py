import tkinter as tk
from tkinter import ttk
import requests

api_key = "ENTER_YOUR_API_KEY_HERE"

list_of_cities = [
    "New York, US",
    "London, UK",
    "Paris, FR",
    "Tokyo, JP",
    "Beijing, CN",
    "Sydney, AU",
    "Dubai, AE",
    "Los Angeles, US",
    "Rome, IT",
    "Berlin, DE",
    "Toronto, CA",
    "Moscow, RU",
    "São Paulo, BR",
    "Istanbul, TR",
    "Bangkok, TH",
    "Mumbai, IN",
    "Seoul, KR",
    "Cairo, EG",
    "Madrid, ES",
    "Johannesburg, ZA",
    "Singapore, SG",
    "Chicago, US",
    "Hong Kong, HK",
    "Buenos Aires, AR",
    "Amsterdam, NL",
    "Vienna, AT",
    "Zurich, CH",
    "Nairobi, KE",
    "San Francisco, US",
    "Kuala Lumpur, MY",
    "Lisbon, PT",
    "Athens, GR",
    "Warsaw, PL",
    "Prague, CZ",
    "Hanoi, VN",
    "Stockholm, SE",
    "Budapest, HU",
    "Copenhagen, DK",
    "Brussels, BE",
    "Manila, PH",
    "Dublin, IE",
    "Vancouver, CA",
    "Doha, QA",
    "Jakarta, ID",
    "Auckland, NZ",
    "Reykjavik, IS",
    "Lima, PE",
    "Tel Aviv, IL",
    "Casablanca, MA",
    "Cape Town, ZA",
    "Other"
]

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_text.set(
            f"City: {data['location']['name']}\n"
            f"Condition: {data['current']['condition']['text']}\n"
            f"Temperature: {data['current']['temp_f']}°F\n"
            f"Humidity: {data['current']['humidity']}%\n"
            f"Wind: {data['current']['wind_mph']} mph"
        )
    else:
        weather_text.set("Could not retrieve weather data.")

def on_city_change(event):
    if selected_city.get() == "Other":
        custom_city_entry.pack(pady=15)
    else:
        custom_city_entry.delete(0, tk.END)
        custom_city_entry.pack_forget()

def on_get_weather():
    city = selected_city.get()
    if city == "Other":
        city = custom_city_entry.get()
    get_weather(city)

root = tk.Tk()
root.title("Weather App")
root.geometry("300x310")

title = tk.Label(root, text="Weather App", font=("Arial", 24, "bold"))
title.pack(pady=15)

selected_city = tk.StringVar()
city_dropdown = ttk.Combobox(root, textvariable=selected_city, values=list_of_cities, state="readonly", height=10)
city_dropdown.current(0)
city_dropdown.bind("<<ComboboxSelected>>", on_city_change)
city_dropdown.pack(pady=10)

custom_city_entry = tk.Entry(root)

weather_text = tk.StringVar()
weather_label = tk.Label(root, textvariable=weather_text, justify="left")
weather_label.pack(pady=20)

get_weather_button = tk.Button(root, text="Get Weather", command=on_get_weather)
get_weather_button.pack()

get_weather(list_of_cities[0])

root.mainloop()
