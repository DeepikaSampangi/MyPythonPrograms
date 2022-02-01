import requests

api_key = "34ee58694a578e7f8c18874e8f0f0994"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 51.759050,
    "lon": 19.458600,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=OWM_endpoint, params=weather_params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]
for data in hourly_data:
    for i in data["weather"]:
        if i["id"] < 700:
            print("Get an umbrella")
