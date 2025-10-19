from utils.http_methods import HttpMethods

# Базовый url и ключ
base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"

class GoogleMapsApi:
    @staticmethod
    # Создание новой локации
    def create_new_place():
        # Ссылка, которая используется для создания нового ресурса в API
        resource_url = "/maps/api/place/add/json"
        # Собираем ссылку для создания ресурса
        post_url = base_url + resource_url + key
        print(post_url)

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
        post_response = HttpMethods.post(post_url, body)

        # Выводим содержимое ответа
        print(post_response.text)

        # Возвращаем ответ сервера
        return post_response

    @staticmethod
    # Получить новую локацию
    def get_place(place_id):
        # Ссылка для получения ресурса
        resource_url = "/maps/api/place/get/json"
        # Формируем ссылку для получения ресурса
        get_url = base_url + resource_url + key + "&place_id=" + place_id
        print(get_url)

        # Делаем GET запрос по сформированный ссылке
        get_response = HttpMethods.get(get_url)
        print(get_response.text)

        # Возвращаем ответ сервера
        return get_response