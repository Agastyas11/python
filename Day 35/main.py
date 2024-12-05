import requests

api_key = "xxxxx"
api_url = "https://openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": -33.721809,
    "lon": 151.043594,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=api_url, params=weather_params)
response.raise_for_status()
weather_data = response.json

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an Umbrella.")




