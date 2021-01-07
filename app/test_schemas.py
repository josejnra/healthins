import unittest

from pydantic import ValidationError

from app.schemas import Healthins


class HealthinsTest(unittest.TestCase):

    def test_county_and_states(self):
        body_request = {
            "headers": ["NAME"],
            "geography_level": "county",
            "places": "*",
            "for_states": "*",
            "year": 2018
        }
        body_validator = Healthins(**body_request)
        self.assertEqual("*", body_validator.for_states)

    def test_geography_level(self):
        body_request = {
            "headers": ["NAME"],
            "geography_level": "my_city",
            "places": "*",
            "year": 2012
        }
        self.assertRaises(ValidationError, Healthins, **body_request)

    def test_no_for_states_passed(self):
        body_request = {
            "headers": ["NAME"],
            "geography_level": "county",
            "places": "*",
            "year": 2012
        }
        self.assertEqual(Healthins(**body_request).for_states, None)

    def test_no_year_passed(self):
        body_request = {
            "headers": ["NAME"],
            "geography_level": "us",
            "places": "*"
        }
        self.assertRaises(ValidationError, Healthins, **body_request)
