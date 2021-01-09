import unittest

from healthins_api.params_builder import ParamsBuilder


class ParamsBuilderTest(unittest.TestCase):

    def test_us_params(self):
        params = ParamsBuilder('2017') \
            .set_header_params(['NIC_PT', 'NUI_PT', 'name']) \
            .set_for_param('us', '*') \
            .build_params()

        expected_params = '?get=NIC_PT,NUI_PT,NAME&for=us:*&time=2017'
        self.assertEqual(params, expected_params)

    def test_state_params(self):
        params = ParamsBuilder('2017') \
            .set_header_params(['NIC_PT', 'NUI_PT', 'NAME']) \
            .set_for_param('state', '01') \
            .build_params()

        expected_params = '?get=NIC_PT,NUI_PT,NAME&for=state:01&time=2017'
        self.assertEqual(params, expected_params)

    def test_county_with_no_in_param(self):
        params = ParamsBuilder('2017') \
            .set_header_params(['NIC_PT', 'NUI_PT', 'NAME']) \
            .set_for_param('county', '*') \
            .build_params()

        expected_params = '?get=NIC_PT,NUI_PT,NAME&for=county:*&time=2017'
        self.assertEqual(params, expected_params)

    def test_county_with_in_param(self):
        params = ParamsBuilder('2017') \
            .set_header_params(['NIC_PT', 'NUI_PT', 'NAME']) \
            .set_for_param('county', '195', '02') \
            .build_params()

        expected_params = '?get=NIC_PT,NUI_PT,NAME&for=county:195&in=state:02&time=2017'
        self.assertEqual(params, expected_params)
