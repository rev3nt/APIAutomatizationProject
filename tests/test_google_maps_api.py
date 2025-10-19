from requests import Response
from utils.api import GoogleMapsApi


class Test_create_place():
    # Создание новой локации
    def test_create_new_place(self):
        print("Метод POST")
        # Сохраняем ответ сервера, создав новую локацию
        post_response: Response = GoogleMapsApi.create_new_place()

        # Преобразуем ответ в json
        check_post = post_response.json()
        # Извлекаем из него id созданного места
        place_id = check_post.get('place_id')

        print("Метод GET POST")
        # Вызываем метод GET для подтверждения создания ресурса
        get_response: Response = GoogleMapsApi.get_place(place_id)

        print("Метод PUT")
        # Вызываем метод PUT, чтобы изменить данные созданного ресурса
        put_response: Response = GoogleMapsApi.put_place(place_id)

        print("Метод GET PUT")
        # Вызываем метод GET для подтверждения изменения ресурса
        get_response: Response = GoogleMapsApi.get_place(place_id)