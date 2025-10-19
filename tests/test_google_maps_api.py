from requests import Response
from utils.api import GoogleMapsApi


class Test_create_place():
    # Шаг теста - создание новой локации
    def test_create_new_place(self):
        # Сохраняем ответ сервера, создав новую локацию
        post_response: Response = GoogleMapsApi.create_new_place()