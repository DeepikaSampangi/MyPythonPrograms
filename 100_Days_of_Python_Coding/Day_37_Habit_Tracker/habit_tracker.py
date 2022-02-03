import requests

USERNAME = "dsam"
TOKEN = "e1ghtch@rs"

pixela_url = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# pixela_user_resp = requests.post(url=url, json=params)
# print(pixela_user_resp.text)

