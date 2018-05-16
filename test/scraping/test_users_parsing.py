import os
from unittest import TestCase

from scraping.endpoint_users import parse_users_json


class UsersParsingTest(TestCase):
    def read_api_data(self, filename):
        TESTDATA_PATH = os.path.join(os.path.dirname(__file__), 'api_data')

        with open(os.path.join(TESTDATA_PATH, filename), 'r') as json_file:
            return json_file.read()

    def test_should_return_empty_keys_when_users_empty(self):
        result = parse_users_json(self.read_api_data('users_empty.json'))

        self.assertFalse(result['users'])
        self.assertFalse(result['projects'])
