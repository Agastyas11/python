import requests

# API
sheety_api = "https://api.sheety.co/8a03ef81b502c22944219aeacd83bff0/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.raw_data = {}

    def get_data(self):
        response = requests.get(url=sheety_api)
        data = response.json()
        self.raw_data = data["prices"]
        return self.raw_data

    def update_destination_codes(self):
        for city in self.raw_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_api}/{city['id']}",
                json=new_data,
            )
            print(response.text)
