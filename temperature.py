from typing import Dict, List
from urllib.request import urlopen
import json

import numpy as np


def read_data_from_url(url: str) -> Dict:
    response = urlopen(url)
    # try:
    #     response = urlopen(url)
    # except:
    #     # "HTTP Error 500: Internal Server Error"
    #     return []

    return json.loads(response.read())


def extract_daytime_temperature(data: Dict) -> List[float]:
    """Extract daytime temperatures from data.

    Args:
        data (Dict): a dictionary of the structure data["properties"]["periods]

    Returns:
        List[float]: daytime temperatures of a city in the next few days.

    Examples:
    >>> data = {
    ...    "properties": {
    ...        "periods": [
    ...            {"temperature": 1.0, "isDaytime": True},
    ...            {"temperature": 2.0, "isDaytime": True},
    ...            {"temperature": 3.0, "isDaytime": False},
    ...        ]
    ...    }
    ... }
    >>> extract_daytime_temperature(data)
    [1.0, 2.0]
    """
    return [d["temperature"] for d in data["properties"]["periods"] if d["isDaytime"]]


def get_mean_temperature(url: str) -> float:
    data = read_data_from_url(url)
    temp_arr = extract_daytime_temperature(data)
    temp_mean = np.mean(temp_arr)
    return round(temp_mean, ndigits=2)
