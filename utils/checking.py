import json

from requests import Response


class Checking():
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert response.status_code == status_code, f"Провал. Статус код = {str(response.status_code)}"
        print("Успех. Статус код = " + str(response.status_code))

    @staticmethod
    def check_json_token(response: Response, expected_values):
        # Выгружаем в json текст ответа сервера
        json_token = json.loads(response.text)

        # Проверяем соответствует ли список ключей ожидаемым значениям
        assert list(json_token) == expected_values, f"Провал. Не все поля соответствуют ожидаемому результату"
        print("Все поля присутствуют")