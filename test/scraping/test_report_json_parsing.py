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