import requests
from datetime import datetime
GENDER = 'male'
WEIGHT_KG = 87
HEIGHT_CM = 183
AGE = 19

APP_ID = 'app_bd60bc4862f74cd6aea71b78'
APP_KEY = 'nix_live_ONjosWm1hzew7VDVS1TpGBkp4undezZ3'

headers = {
    'x-app-id' : APP_ID,
    'x-app-key' : APP_KEY,
}
exercise_type = input('What exercise did you do ?')
exercise_endpoint = 'https://app.100daysofpython.dev/v1/nutrition/natural/exercise'
sheet_endpoint = 'https://api.sheety.co/5c5c2e049e4b89dd691586a9aa739105/workoutTracking/workouts'
request_body = {
    'query' :exercise_type,
    'weight_kg' : WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age' : AGE,
    'gender' : GENDER
}
sheet_headers = {
    "Authorization": "Basic c2hvaGFiYm9zOlNob2hhYmJvczIwMDck"
}

response = requests.post(url=exercise_endpoint,json=request_body,headers=headers)
result = response.json()

today_date = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')

for exercise in result["exercises"]:
    sheet_inputs ={
        'workout':{
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    sheet_reesponse = requests.post(url=sheet_endpoint,json=sheet_inputs,headers=sheet_headers)
    print(sheet_reesponse.text)
    








