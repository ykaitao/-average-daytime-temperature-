from src.temperature import get_average_daytime_temperature


# URLs
urls = {
    "Salt Lake City, Utah": "https://api.weather.gov/gridpoints/SLC/99,174/forecast",
    "Denver, Colorado": "https://api.weather.gov/gridpoints/BOU/58,60/forecast",
    "Phoenix, Arizona": "https://api.weather.gov/gridpoints/PSR/157,64/forecast",
    "Tampa, Florida": "https://api.weather.gov/gridpoints/TBW/70,98/forecast",
}


for city, url in urls.items():
    print(f"{city} Average Temp: {get_average_daytime_temperature(url)}")
