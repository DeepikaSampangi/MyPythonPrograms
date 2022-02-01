import http
import requests

api_key = "34ee58694a578e7f8c18874e8f0f0994"

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={api_key}")
response.raise_for_status()
print(response.json())
