import requests

api_key = "34ee58694a578e7f8c18874e8f0f0994"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key
}
response = requests.get(url=OWM_endpoint, params=weather_params)
response.raise_for_status()
print(response.status_code)
print(response.json())
