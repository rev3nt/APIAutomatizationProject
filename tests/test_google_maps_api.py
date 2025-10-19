from requests import Response
from utils.api import GoogleMapsApi
from utils.checking import Checking


class TestCreatePlace():
    # Создание новой локации
    def test_create_new_place(self):
        print("Метод POST")
        # Сохраняем ответ сервера, создав новую локацию
        post_response: Response = GoogleMapsApi.create_new_place()
        # Добавляем проверку на статус код
        Checking.check_status_code(post_response, 200)
        Checking.check_json_token(post_response, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(post_response, 'status', 'OK')
        Checking.check_json_for_word(post_response, 'scope', 'APP')

        # Преобразуем ответ в json
        check_post = post_response.json()
        # Извлекаем из него id созданного места
        place_id = check_post.get('place_id')

        print("Метод GET POST")
        # Вызываем метод GET для подтверждения создания ресурса
        get_response: Response = GoogleMapsApi.get_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(get_response, 200)
        Checking.check_json_token(get_response,['location', 'accuracy', 'name', 'phone_number',
                                                'address', 'types', 'website', 'language'])
        Checking.check_json_value(get_response, 'accuracy', '50')
        Checking.check_json_for_word(get_response, 'name', 'house')

        print("Метод PUT")
        # Вызываем метод PUT, чтобы изменить данные созданного ресурса
        put_response: Response = GoogleMapsApi.put_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(put_response, 200)
        Checking.check_json_token(put_response, ['msg'])
        Checking.check_json_value(put_response, 'msg', 'Address successfully updated')
        Checking.check_json_for_word(put_response, 'msg', 'updated')

        print("Метод GET PUT")
        # Вызываем метод GET для подтверждения изменения ресурса
        get_response: Response = GoogleMapsApi.get_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(get_response, 200)
        Checking.check_json_token(get_response,['location', 'accuracy', 'name', 'phone_number',
                                                'address', 'types', 'website', 'language'])
        Checking.check_json_value(get_response, 'address', '100 Lenina street, RU')
        Checking.check_json_for_word(get_response, 'accuracy', '50')

        print("Метод DELETE")
        # Удаляем созданный ресурс с помощью DELETE
        delete_response: Response = GoogleMapsApi.delete_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(delete_response, 200)
        Checking.check_json_token(delete_response, ['status'])
        Checking.check_json_value(delete_response, 'status', 'OK')
        Checking.check_json_for_word(delete_response, 'status', 'OK')

        print("Метод GET DELETE")
        # Пробуем получить удаленный ресурс
        get_response: Response = GoogleMapsApi.get_place(place_id)
        # Добавляем проверку на статус код
        Checking.check_status_code(get_response, 404)
        Checking.check_json_token(get_response, ['msg'])
        Checking.check_json_value(get_response, 'msg', 'Get operation failed, looks like place_id  doesn\'t exists')
        Checking.check_json_for_word(get_response, 'msg', 'failed')

        print("Тестирование добавления, изменения и удаления новой локации прошло успешно!")