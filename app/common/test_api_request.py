import unittest
from unittest.mock import patch

import requests

from app.common.api_request import APIRequest


class ResponseObjectMock:
    pass


class APIRequestTest(unittest.TestCase):

    @patch('app.common.api_request.requests.get')
    def test_healthins_get_successful(self, get_method):
        response_object_mock = ResponseObjectMock()
        setattr(response_object_mock, 'text', '[["NIC_PT", "NUI_PT", "time", "state", "county"], ["133987", "9173", "2017", "10", "001"]]')
        setattr(response_object_mock, 'status_code', 200)

        get_method.return_value = response_object_mock
        response = APIRequest.get_data('ABC')
        self.assertEqual(response, [['NIC_PT', 'NUI_PT', 'time', 'state', 'county'], ['133987', '9173', '2017', '10', '001']])

    @patch('app.common.api_request.requests.get')
    def test_healthins_wrong_response_code(self, get_method):
        response_object_mock = ResponseObjectMock()
        setattr(response_object_mock, 'text', 'error: unexpected hour in date/time predicate: time')
        setattr(response_object_mock, 'status_code', 400)

        get_method.return_value = response_object_mock
        self.assertRaises(requests.exceptions.RequestException, APIRequest.get_data, 'ABC')
