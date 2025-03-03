import requests
from datetime import datetime
import os

HOST = "https://trackapi.nutritionix.com"
NLE_ENDPOINT = "/v2/natural/exercise"
NUTRITION_APP_ID = os.getenv("NUTRITION_APP_ID")
NUTRITION_API_KEY = os.getenv("NUTRITION_API_KEY")

BEARER = os.getenv("API_BEARER_SHEETY")
PROJECT = "workouts"
SHEET = "workouts"

GENDER = "Male"
WEIGHT_KG = 65
HEIGHT_CM = 163
AGE = 32

# exercise_inp = input("Tell me which exercises you did: ")

params = {
    # "query": exercise_inp,
    "query": "swimming for an hour",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

headers = {
    "x-app-id": NUTRITION_APP_ID,
    'x-app-key': NUTRITION_API_KEY

}

# datetime = datetime.now()

response = requests.post(url=HOST+NLE_ENDPOINT, json=params, headers=headers)
response = response.json()
print(response)
# exercises = response["exercises"]
# print(exercises)

datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(datetime)
