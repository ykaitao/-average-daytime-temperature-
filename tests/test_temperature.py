import pytest

from src.temperature import extract_daytime_temperature

# test function extract_daytime_temperature
class TestExtractDaytimeTemperature:
    def test_invalid_inputs(self):
        with pytest.raises(AssertionError):
            extract_daytime_temperature(data="string_input")  # input is not dict
            extract_daytime_temperature(data={})
            extract_daytime_temperature(data={"properties": {}})

    def test_empty_periods(self):
        data = {"properties": {"periods": []}}
        assert [] == extract_daytime_temperature(data=data)

    def test_valid_inputs(self):
        data = {
            "properties": {
                "periods": [
                    {"temperature": 1.0, "isDaytime": True},
                    {"temperature": 2.0, "isDaytime": True},
                    {"temperature": 3.0, "isDaytime": False},
                ]
            }
        }
        assert [1.0, 2.0] == extract_daytime_temperature(data=data)
