# 1xx: Hold On
# 2xx: Here you go
# 3xx: Go Away
# 4xx: You Screwed Up
# 5xx: I screwed Up

import requests
import time
from datetime import datetime

MY_LAT = 20
MY_LONG = 78


def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    iss_position = (longitude, latitude)

    if iss_position[0] in range(MY_LAT - 5, MY_LAT + 5) and iss_position[1] in range(
        MY_LONG - 5, MY_LONG + 5
    ):
        return True


def is_dark():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters
    )
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset <= time_now.hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_above() and is_dark():
        print("Look Up in the Sky, Sent over email")
