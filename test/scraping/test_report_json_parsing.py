import os
from unittest import TestCase

from scraping.endpoint_reports import parse_reports_json
from scraping.types import UserKey, ProjectKey

USER1 = UserKey(311716, "USER1")
USER2 = UserKey(311717, "USER2")
USER3 = UserKey(311718, "USER3")
PROJECT1 = ProjectKey(434418, "PROJECT1")
PROJECT2 = ProjectKey(434419, "PROJECT2")
PROJECT3 = ProjectKey(434420, "PROJECT3")


class ReportsParsingTest(TestCase):
    def read_api_data(self, filename):
        TESTDATA_PATH = os.path.join(os.path.dirname(__file__), 'api_data')

        with open(os.path.join(TESTDATA_PATH, filename), 'r') as json_file:
            return json_file.read()

    def test_should_parse_empty_list(self):
        result = parse_reports_json(self.read_api_data('report_empty.json'))

        self.assertEqual(result, [])

    def test_should_parse_duration_for_one_project_one_user(self):
        result = parse_reports_json(self.read_api_data('report_one_user_one_project.json'))

        self.assertEqual(result, [
            (PROJECT1, USER1, 10)
        ])

    def test_should_parse_duration_for_one_user_two_projects(self):
        result = parse_reports_json(self.read_api_data('report_one_user_two_projects.json'))

        self.assertEqual(result, [
            (PROJECT1, USER1, 10),
            (PROJECT2, USER1, 10)
        ])

    def test_should_parse_duration_for_two_users_one_project(self):
        result = parse_reports_json(self.read_api_data('report_two_users_one_project.json'))

        self.assertEqual(result, [
            (PROJECT1, USER1, 5),
            (PROJECT1, USER2, 5)
        ])

    def test_should_parse_duration_for_three_users_three_projects(self):
        result = parse_reports_json(self.read_api_data('report_three_users_three_projects.json'))

        self.assertEqual(result, [
            (PROJECT1, USER1, 5),
            (PROJECT1, USER2, 5),
            (PROJECT2, USER1, 10),
            (PROJECT3, USER2, 3),
            (PROJECT3, USER3, 7),
        ])