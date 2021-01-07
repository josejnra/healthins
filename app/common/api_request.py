import json
from typing import List

import requests

from app.common.data_source_abstract import DataSourceAbstract


class APIRequest(DataSourceAbstract):

    def get(self, url: str) -> List[list]:
        response = requests.get(url=url)

        if response.status_code != 200:
            raise requests.exceptions.RequestException(response.text)

        return json.loads(response.text)
