import requests
from datetime import datetime

USERNAME="sony-j"
TOKEN="1c8046ab438c4443955306431c6ee219"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    "thanksCode":"its working"
        }

graph_create = {
    "id": GRAPH_ID,
    "name": "coding",
    "unit": "commit",
    "type": "int",
    "color": "momiji",
    "timezone": "Asia/Kolkata"
        }

graph_update = {
    "name": "coding",
    "unit": "commit",
    "color": "momiji",
    "timezone": "Asia/Kolkata",
    "publishOptionalData": True
        }
update_commit_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

date_today = datetime(year=2023, month=3, day=10)

post_pixel_data = {
    "date": date_today.strftime("%Y%m%d"),
    "quantity": input("How many commits ? "),
    }
# print(post_pixel_data)

headers = {
    "X-USER-TOKEN": TOKEN
}


update_pixel_data = {
    "quantity":"40",
    }
update_commit_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

update_pixel_endpoint = f"{update_commit_url}/{date_today.strftime('%Y%m%d')}"
print(update_pixel_endpoint)


# response = requests.post(url=pixela_endpoint, json=params)
# print(response.json())

# response = requests.post(url=graph_endpoint, json=graph_create, headers=headers)
# print(response.json())

# response = requests.put(url=update_endpoint_graph, json=graph_update, headers=headers)
# print(response.status_code)

# response = requests.post(url=update_commit_url, json=post_pixel_data, headers=headers)
# print(response.status_code)

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.status_code)
# print(response.json())

del_response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(del_response.status_code)
print(del_response.json())