# Taranis

Python API wrapper for [weather-api](https://github.com/robertoduessmann/weather-api).

## Installation:

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):

```
pip install -U taranis
```

## Usage:

```python
>>> taranis.get_weather('San Francisco')
{'temperature': '+15 °C', 'wind': '24 km/h', 'description': 'Partly cloudy', 'forecast': [{'day': '1', 'temperature': '20 °C', 'wind': '18 km/h'}, {'day': '2', 'temperature': '16 °C', 'wind': '22 km/h'}, {'day': '3', 'temperature': '17 °C', 'wind': '12 km/h'}]}
```

```python
>>> taranis.get_temperature('San Francisco')
'+15 °C'
```

```python
>>> taranis.get_wind('San Francisco')
'24 km/h'
```

```python
>>> taranis.get_description('San Francisco')
'Partly cloudy'
```

```python
>>> taranis.get_forecast('San Francisco')
[{'day': '1', 'temperature': '20 °C', 'wind': '18 km/h'}, {'day': '2', 'temperature': '16 °C', 'wind': '22 km/h'}, {'day': '3', 'temperature': '17 °C', 'wind': '12 km/h'}]
```