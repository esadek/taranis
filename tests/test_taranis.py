import taranis

CITY = "Oakland"


class TestTaranis:
    def test_get_weather(self):
        weather = taranis.get_weather(CITY)
        assert type(weather) == dict
        for key in ["temperature", "wind", "description", "forecast"]:
            assert key in weather

    def test_get_temperature(self):
        temperature = taranis.get_temperature(CITY)
        assert type(temperature) == str
        assert temperature.endswith("°C")

    def test_get_wind(self):
        wind = taranis.get_wind(CITY)
        assert type(wind) == str
        assert wind.endswith("km/h")

    def test_get_description(self):
        description = taranis.get_description(CITY)
        assert type(description) == str

    def test_get_forecast(self):
        forecast = taranis.get_forecast(CITY)
        assert type(forecast) == list
        assert type(forecast[0]) == dict
        for key in ["day", "temperature", "wind"]:
            assert key in forecast[0]
