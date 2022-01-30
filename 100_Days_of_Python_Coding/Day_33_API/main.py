# 1xx: Hold On
# 2xx: Here you go
# 3xx: Go Away
# 4xx: You Screwed Up
# 5xx: I screwed Up

import requests
from datetime import  datetime

MY_LAT = 51.507351
MY_LONG = -0.127758
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunset)
time_now = datetime.now()
print(time_now)
