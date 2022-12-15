from urllib.request import urlopen
from typing import Dict, List
import numpy as np
import json

# URLs
urls = {
    "Salt Lake City, Utah": "https://api.weather.gov/gridpoints/SLC/99,174/forecast",
    "Denver, Colorado": "https://api.weather.gov/gridpoints/BOU/58,60/forecast",
    "Phoenix, Arizona": "https://api.weather.gov/gridpoints/PSR/157,64/forecast",
    "Tampa, Florida": "https://api.weather.gov/gridpoints/TBW/70,98/forecast",
}


def read_data_from_url(url: str) -> Dict:

    response = urlopen(url)

    return json.loads(response.read())


def extract_daytime_temperature(data: Dict) -> List[float]:
    return [d["temperature"] for d in data["properties"]["periods"] if d["isDaytime"]]


def get_mean_temperature(url: str) -> float:
    data = read_data_from_url(url)
    temp_arr = extract_daytime_temperature(data)
    temp_mean = np.mean(temp_arr)
    return round(temp_mean, ndigits=2)


for city, url in urls.items():
    print(f"{city} Average Temp: {get_mean_temperature(url)}")
