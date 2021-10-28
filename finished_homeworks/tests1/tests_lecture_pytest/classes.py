import requests


class ClassForTest:
    @staticmethod
    def send_request():
        response = requests.get("https://jsonplaceholder.typicode.com/tsodos")
        return response
