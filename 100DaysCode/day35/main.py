import os

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

owm_api_key = os.environ.get("owm_api_key")
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
twilio_account_sid = os.environ.get("twilio_account_sid")
twilio_auth_token = os.environ.get("twilio_auth_token")

parameters = {
    "lat": "6.524379",
    "lon": "3.379206",
    "appid": owm_api_key,
    "cnt": 4
}

response = requests.get(endpoint, params=parameters)
weather_data = response.json()
weather_data = weather_data
# weather_id = weather_data["list"][0]["weather"]
# print(weather_id)

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(twilio_account_sid, twilio_auth_token,
                    # http_client=proxy_client
                    )

    message = client.messages \
        .create(
        body="Its raining in Lagos, get an umbrella",
        from_='+13235534389',
        to='+917276365937'
    )

    print(message.sid)
    print(message.status)
# "https://api.openweathermap.org/data/2.5/weather?q=London,uk&callback=test&appid=2fbf9955dcd041f40fe2cbc923766d83"
