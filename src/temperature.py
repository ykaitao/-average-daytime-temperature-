from typing import Dict, List
from urllib.request import urlopen
import json

import numpy as np


def read_data_from_url(url: str) -> Dict:
    """Read data from a url.

    Args:
        url (str): the url of data.

    Returns:
        Dict: data from the url.
    """
    try:
        response = urlopen(url)
    except:
        # "HTTP Error 500: Internal Server Error"
        print("Please check your internet connection and retry.")
        return {}

    return json.loads(response.read())


def check_data_format(data: Dict) -> None:
    """Check if the wheather data is of the expected format.

    Args:
        data (Dict): wheather data of a city, which expected to be a nested
        dictionary in the following structure: `data->properties->periods`.
    """
    assert isinstance(data, dict)  # data is a dict
    assert "properties" in data
    assert "periods" in data["properties"]
    assert isinstance(data["properties"]["periods"], list)  # `periods` is a list


def extract_daytime_temperature(data: Dict) -> List[float]:
    """Extract daytime temperatures from the weather data.

    Args:
        data (Dict): weather data of a city.

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
    check_data_format(data)
    return [d["temperature"] for d in data["properties"]["periods"] if d["isDaytime"]]


def get_average_daytime_temperature(url: str) -> float:
    """Get average daytime temperacture of a city from its weather url.

    Args:
        url (str): weather url of a city

    Returns:
        float: average daytime temperacture of a city
    """
    data = read_data_from_url(url)
    temp_arr = extract_daytime_temperature(data)
    assert len(temp_arr) > 0, "at least one day of temperature should be extracted."
    temp_mean = np.mean(temp_arr)
    return round(temp_mean, ndigits=2)
