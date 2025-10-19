from requests import Response
from utils.api import GoogleMapsApi
from utils.checking import Checking


class Test_create_place():
    # Создание новой локации
    def test_create_new_place(self):
        print("Метод POST")
        # Сохраняем ответ сервера, создав новую локацию
        post_response: Response = GoogleMapsApi.create_new_place()
        # Добавляем проверку на статус код
        Checking.check_status_code(post_response, 200)

        # Преобразуем ответ в json
        check_post = post_response.json()
        # Извлекаем из него id созданного места
        place_id = check_post.get('place_id')

        print("Метод GET POST")
        # Вызываем метод GET для подтверждения создания ресурса
        get_response: Response = GoogleMapsApi.get_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(get_response, 200)

        print("Метод PUT")
        # Вызываем метод PUT, чтобы изменить данные созданного ресурса
        put_response: Response = GoogleMapsApi.put_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(put_response, 200)

        print("Метод GET PUT")
        # Вызываем метод GET для подтверждения изменения ресурса
        get_response: Response = GoogleMapsApi.get_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(get_response, 200)

        print("Метод DELETE")
        # Удаляем созданный ресурс с помощью DELETE
        delete_response: Response = GoogleMapsApi.delete_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(delete_response, 200)

        print("Метод GET DELETE")
        # Пробуем получить удаленный ресурс
        get_response: Response = GoogleMapsApi.get_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(get_response, 404)