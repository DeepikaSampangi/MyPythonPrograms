import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
print(response.json())

# 1xx: Hold On
# 2xx: Here you go
# 3xx: Go Away
# 4xx: You Screwed Up
# 5xx: I screwed Up
