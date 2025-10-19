import requests

# Создаем класс с катомными http методами
class HttpMethods:
    # Создаем хранилище для заголовков и куки
    headers = {"Content-Type": "application/json"}
    cookie = ""

    # Методы в классе будут статическими, чтобы они не были привязаны к конкретному классу
    @staticmethod
    # Создаем метод GET
    def get(url):
        # Получаем ответ сервера
        response = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        # Возвращаем его
        return response

    @staticmethod
    # Метод POST
    def post(url, body):
        # В этом и следующих запросах есть возможность отправить тело
        response = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        return response

    @staticmethod
    # Метод PUT
    def put(url, body):
        response = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        return response

    @staticmethod
    # Метод DELETE
    def delete(url, body):
        response = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        return response