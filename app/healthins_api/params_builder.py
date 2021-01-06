from typing import List


class ParamsBuilder:

    def __init__(self, year: str):
        self._get = None
        self._for = None
        self._in = None
        self._time = 'time=' + year

    def set_header_params(self, headers: List[str]):
        self._get = 'get=' + ','.join([header.upper() for header in headers])
        return self

    def set_for_param(self, geography_level: str, place: str, state: str = None):
        is_county = {
            'us': False,
            'state': False,
            'county': True
        }.get(geography_level)

        self._for = 'for=' + geography_level + ':' + place

        if is_county and state:
            self._in = 'in=state' + ':' + state

        return self

    def build_params(self) -> str:
        in_param = f"&{self._in}" if self._in else ''
        return f"?{self._get}&{self._for}{in_param}&{self._time}"
