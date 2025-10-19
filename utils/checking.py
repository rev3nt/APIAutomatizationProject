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

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        # Преобразуем ответ сервера в json
        check = response.json()

        # Извлекаем значение из необходимого поля
        get_value = check.get(field_name)

        # Проверяем соответствует ли полученное значение ожидаемому результату
        assert get_value == expected_value, f"Значение {expected_value} не обнаружено в поле {field_name}"
        print(f"Значение {expected_value} находится в {field_name}")

    @staticmethod
    def check_json_for_word(response: Response, field_name, search_word):
        # Преобразуем ответ сервера в json
        check = response.json()

        # Получаем значение нужного поля
        get_value = check.get(field_name)

        # Проверяем, есть ли слово в поле
        if search_word in get_value:
            print(f"Слово {search_word} есть в поле {field_name}")
        else:
            print(f"Слово {search_word} не обнаружено в поле {field_name}")