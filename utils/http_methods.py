import requests


class HttpMethods:
    headers = {"Content-Type": "application/json"}
    cookie = ""

    @staticmethod
    def get(url):
        response = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        return response

    @staticmethod
    def post(url, body):
        response = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        return response

    @staticmethod
    def put(url, body):
        response = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        return response

    @staticmethod
    def delete(url, body):
        response = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)

        return response