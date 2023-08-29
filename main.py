import os
from datetime import datetime
import requests

GENDER = "male"
WEIGHT_KG = 69
HEIGHT_CM = 180
AGE = 19

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

NUTRITION_APP_ID = os.environ["NUTRITION_APP_ID"]
NUTRITION_API_KEY = os.environ["NUTRITION_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
# ------------------------------------------------- SHEETY CODE ---------------------------------------------------
sheet_endpoint = "https://api.sheety.co/52c2de514e0e14e040248ee2b2dcaf46/myWorkouts/workouts"

TODAY = datetime.now()
DATE = TODAY.strftime("%d/%m/%Y")
TIME = TODAY.strftime("%X")
for exercise in result['exercises']:
    sheet_params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_params, auth=(USERNAME, PASSWORD))
    print(sheet_response.text)
