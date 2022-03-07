import requests
import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)


api_key = os.environ["api_key"]
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 51.759050,
    "lon": 19.458600,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(url=OWM_endpoint, params=weather_params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    for data in hour_data["weather"]:
        condition_code = data["id"]
        if condition_code < 700:
            will_rain = True

if will_rain:
    message = client.messages.create(
        body="Remember to bring an Umbrella", from_="+15017122661", to="+15558675310"
    )
