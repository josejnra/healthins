import json

import requests


class APIRequest:

    @staticmethod
    def get_data(url: str):
        response = requests.get(url=url)

        if response.status_code != 200:
            raise requests.exceptions.RequestException(response.text)

        return json.loads(response.text)
