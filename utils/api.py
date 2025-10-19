from utils.http_methods import HttpMethods


base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"

class GoogleMapsApi:
    @staticmethod
    def create_new_place():
        print("Метод POST")

        resource_url = "/maps/api/place/add/json"
        create_location_url = base_url + resource_url + key
        print(create_location_url)

        body = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park", "shop"
            ], "website": "http://google.com",
            "language": "French-IN"
        }

        response = HttpMethods.post(create_location_url, body)
        print("Ответ сервера получен")

        print(response.text)

        return response