import os
from unittest import TestCase

from scraping.endpoint_users import parse_users_json
from scraping.types import UserKey, ProjectKey

USER1 = UserKey(311716, "NAME A")
USER2 = UserKey(196435, "NAME B")
USER3 = UserKey(202111, "NAME C")
PROJECT1 = ProjectKey(434418, "hubstaff bot36")
PROJECT2 = ProjectKey(434419, "Project A")
PROJECT3 = ProjectKey(434420, "Project B")


class UsersParsingTest(TestCase):
    def read_api_data(self, filename):
        TESTDATA_PATH = os.path.join(os.path.dirname(__file__), 'api_data')

        with open(os.path.join(TESTDATA_PATH, filename), 'r') as json_file:
            return json_file.read()

    def test_should_return_empty_keys_when_users_empty(self):
        result = parse_users_json(self.read_api_data('users_empty.json'))

        self.assertEqual(result['users'], set())
        self.assertEqual(result['projects'], set())

    def test_should_return_user_key_for_single_user_without_project(self):
        result = parse_users_json(self.read_api_data('users_one_no_projects.json'))

        self.assertEqual(result['users'], {USER1})
        self.assertEqual(result['projects'], set())

    def test_should_return_project_keys_for_single_user_with_three_projects(self):
        result = parse_users_json(self.read_api_data('users_one_3_projects.json'))

        self.assertEqual(result['users'], {USER1})
        self.assertEqual(result['projects'], {PROJECT1, PROJECT2, PROJECT3})
