from utils.http_methods import HttpMethods

# Базовый url и ключ
base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"

class GoogleMapsApi:
    @staticmethod
    # Создание новой локации
    def create_new_place():
        print("Метод POST")

        # Ссылка, которая используется для создания нового ресурса в API
        resource_url = "/maps/api/place/add/json"
        # Собираем ссылку для создания ресурса
        create_location_url = base_url + resource_url + key
        print(create_location_url)

        # Тело запроса
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

        # Получаем ответ от сервера на запрос по ссылке, также передаем в запрос тело
        response = HttpMethods.post(create_location_url, body)
        print("Ответ сервера получен")

        # Выводим содержимое ответа
        print(response.text)

        # Возвращаем ответ
        return response