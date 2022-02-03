import requests
from datetime import datetime as dt

USERNAME = "dsam"
TOKEN = "e1ghtch@rs"
GRAPH_ID = "graph1"

pixela_url = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# pixela_user_resp = requests.post(url=url, json=params)
# print(pixela_user_resp.text)

graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": " Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color":"ajisai"
}

auth_header = {
    "X-USER-TOKEN": TOKEN
}
# graph_resp = requests.post(url=graph_endpoint, json=graph_config, headers=auth_header)
# print(graph_resp.text)

pixel_endpoint = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": "20220202",
    "quantity": "5.0"
}
pixel_resp = requests.post(url=pixel_endpoint, json=pixel_config, headers=auth_header)
print(pixel_resp.text)