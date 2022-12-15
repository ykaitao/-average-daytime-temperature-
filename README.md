# average-daytime-temperature
Using the weather API api.weather.gov, find the average daytime temperature in four cities (Salt Lake City, Denver, Phoenix, and Tampa).

## Install required packages
```bash
>>> pip install -r requirements.txt
```

## Run main.py
```bash
>>> python main.py
Salt Lake City, Utah Average Temp: 31.0
Denver, Colorado Average Temp: 40.14
Phoenix, Arizona Average Temp: 60.43
Tampa, Florida Average Temp: 69.57
```

## Run pytest
```bash
>>> pytest
==================================================== test session starts =====================================================
platform linux -- Python 3.7.4, pytest-7.2.0, pluggy-1.0.0
rootdir: /media/ktyang/D1/Projects/average-daytime-temperature, configfile: pytest.ini
collected 4 items                                                                                                            

src/temperature.py .                                                                                                   [ 25%]
tests/test_temperature.py ...                                                                                          [100%]

===================================================== 4 passed in 0.59s ======================================================
```
