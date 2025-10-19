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

    @staticmethod
    def put_place(place_id):
        # Ссылка для обновления ресурса
        resource_url = "/maps/api/place/update/json"
        # Формируем URL для отправления PUT запроса
        put_url = base_url + resource_url + key

        # Тело запроса с полем, которое будет изменено по переданному в функцию place_id
        body = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        # Отправляем PUT запрос по сформированному URL и body
        put_response = HttpMethods.put(put_url, body)
        print(put_response.text)

        # Возвращаем ответ сервера на PUT запрос
        return put_response

    @staticmethod
    def delete_place(place_id):
        # Ссылка на ресурс для удаления
        resource_url = "/maps/api/place/delete/json"
        # Собираем ссылку для выполнения DELETE
        delete_url = base_url + resource_url + key
        print(delete_url)

        # Тело запроса с нужным place_id
        body = {
            "place_id": place_id,
        }

        # Отправляем запрос на удаление по сформированному URL и body
        delete_response = HttpMethods.delete(delete_url, body)
        print(delete_response.text)

        # Возвращаем ответ сервера
        return delete_response
