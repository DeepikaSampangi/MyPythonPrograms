from datetime import datetime as dt

import requests

USERNAME = "dsam"
TOKEN = "e1ghtch@rs"
GRAPH_ID = "graph1"

pixela_url = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# pixela_user_resp = requests.post(url=url, json=params)
# print(pixela_user_resp.text)

graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": " Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

auth_header = {"X-USER-TOKEN": TOKEN}
# graph_resp = requests.post(url=graph_endpoint, json=graph_config, headers=auth_header)
# print(graph_resp.text)

today = dt.now().date()
pixel_endpoint = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {"date": today.strftime("%Y%m%d"), "quantity": "2.5"}
# pixel_resp = requests.post(url=pixel_endpoint, json=pixel_config, headers=auth_header)
# print(pixel_resp.text)

## Update a Pixel

update_pixel_data = {"quantity": "6.0"}
# update_pixel_resp = requests.put(url=f"{pixel_endpoint}/20220202", json=update_pixel_data, headers=auth_header)
# print(update_pixel_resp.text)

## Delete a Pixel

delete_endpoint = f"{pixel_endpoint}/20220202"

delete_resp = requests.delete(url=delete_endpoint, headers=auth_header)
print(delete_resp.text)
