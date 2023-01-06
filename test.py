import requests

url = 'http://api.plos.org/search?q=title:DNA'
response = requests.get(url=url)
# body = response.content
body_json = response.json()
body = body_json['response']['docs']
# response_dict = str(json.loads(response.text))
# print(response_dict)

for ctr in range(len(body)):
  print(body[ctr]['author_display'])
# for body_obj in body:
#     print(body_obj)

# print(len(body_json['response']['docs']))
