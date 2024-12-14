import requests
from datetime import *

# site parameters
url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_url = "https://api.sheety.co/ /myWorkouts/workouts"
app_id = 
app_key = 

# personal data
metric_weight = 
metric_height = 
age = 
gender = 

# description of exercise
exercise_query = input("What exercises did you do mate?: ")

# response params
parameters = {
    "query": exercise_query,
    "gender": gender,
    "weight_kg": metric_weight,
    "height_cm": metric_height,
    "age": age
}
headers = {
    "x-app-id": app_id,
    "x-app-key": app_key
}

# posting data from nutritionix
response = requests.post(url, json=parameters, headers=headers)
data = response.json()

print(data)

# assigning data
date = datetime.now().strftime("%Y-%m-%d")
time = datetime.now().strftime("%H:%M:%S")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


# posting data to spreadsheet
sheety_post = requests.post(sheety_url, json=sheet_inputs)
print(sheety_post.text)


