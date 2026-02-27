import requests

GENDER = 'male'
WEIGHT_KG = 87
HEIGHT_CM = 183
AGE = 19

APP_ID = 'app_bd60bc4862f74cd6aea71b78'
API_KEY = 'nix_live_ONjosWm1hzew7VDVS1TpGBkp4undezZ3'

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
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
print(response.text)