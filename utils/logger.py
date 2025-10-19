import datetime
import os

from requests import Response

class Logger:
    # Формируем название файла из текущей даты в определенном формате
    file_name = f'./logs/log_{str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}.log'

    # Метод для записи в файл
    @classmethod
    def write_log_to_file(cls, data:str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    # Метод для записи информации о запросе
    @classmethod
    def write_request(cls, url: str, method: str):
        # Достаем название проводимого теста
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        # Сохраняем название теста, дату, http метод и URL
        data_to_add = f'\n-----\n'
        data_to_add += f'Test name: {test_name}\n'
        data_to_add += f'Time: {datetime.datetime.now()}\n'
        data_to_add += f'Request method: {method}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += f'\n'

        # Передаем данные для записи в файл
        cls.write_log_to_file(data_to_add)

    # Метод для логирования ответа сервера
    @classmethod
    def write_response(cls, result: Response):
        # Достаем и сохраняем заголовки и куки запроса
        headers_as_dict = dict(result.headers)
        cookies_as_dict = dict(result.cookies)

        # Сохраняем статус-код, текст ответа, заголовки и куки
        data_to_add = f'\n-----\n'
        data_to_add += f'Response code: {result.status_code}\n'
        data_to_add += f'Response text: {result.text}\n'
        data_to_add += f'Response headers: {headers_as_dict}\n'
        data_to_add += f'Response cookies: {cookies_as_dict}\n'
        data_to_add += f'\n-----\n'

        # Передаем данные для записи в лог
        cls.write_log_to_file(data_to_add)