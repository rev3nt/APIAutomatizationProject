from requests import Response
from utils.api import GoogleMapsApi


class Test_create_place():
    def test_create_new_place(self):
        post_response: Response = GoogleMapsApi.create_new_place()