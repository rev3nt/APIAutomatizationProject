from utils.logger import Logger

import requests

# Создаем класс с кастомными http методами
class HttpMethods:
    # Создаем хранилище для заголовков и куки
    headers = {"Content-Type": "application/json"}
    cookie = ""

    # Методы в классе будут статическими, чтобы они не были привязаны к конкретному классу
    @staticmethod
    # Создаем метод GET
    def get(url):
        # Добавляем запрос в лог
        Logger.write_request(url, method="GET")
        # Получаем ответ сервера
        response = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        # Записываем данные ответа в лог
        Logger.write_response(response)

        # Возвращаем его
        return response

    @staticmethod
    # Метод POST
    def post(url, body):
        Logger.write_request(url, method="POST")
        # В этом и следующих запросах есть возможность отправить тело
        response = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.write_response(response)

        return response

    @staticmethod
    # Метод PUT
    def put(url, body):
        Logger.write_request(url, method="PUT")
        response = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.write_response(response)

        return response

    @staticmethod
    # Метод DELETE
    def delete(url, body):
        Logger.write_request(url, method="DELETE")
        response = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.write_response(response)

        return response