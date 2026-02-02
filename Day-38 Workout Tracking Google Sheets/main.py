import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 165
AGE = 26

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/31d57638cc25779494fffeaeb935d84c/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": 70,
    "height_cm": 175,
    "age":30,
    "gender":"male"
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)


