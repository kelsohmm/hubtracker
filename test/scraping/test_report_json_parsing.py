import os
from unittest import TestCase
from scraping.activity_report import get_report_entries_from_json
from scraping.types import ReportEntry
from test.scraping.data_common import *

TIME_5SEC_INT = 5
TIME_3SEC_INT = 3
TIME_7SEC_INT = 7


class ReportsParsingTest(TestCase):
    def read_api_data(self, filename):
        TESTDATA_PATH = os.path.join(os.path.dirname(__file__), 'api_data')

        with open(os.path.join(TESTDATA_PATH, filename), 'r') as json_file:
            return json_file.read()

    def test_should_parse_empty_list(self):
        result = get_report_entries_from_json(self.read_api_data('report_empty.json'))

        self.assertEqual(result, [])

    def test_should_parse_duration_for_one_project_one_user(self):
        result = get_report_entries_from_json(self.read_api_data('report_one_user_one_project.json'))

        self.assertEqual(result, [
            ReportEntry(PROJECT1, USER1, TIME_10SEC_INT)
        ])

    def test_should_parse_duration_for_one_user_two_projects(self):
        result = get_report_entries_from_json(self.read_api_data('report_one_user_two_projects.json'))

        self.assertEqual(result, [
            ReportEntry(PROJECT1, USER1, TIME_10SEC_INT),
            ReportEntry(PROJECT2, USER1, TIME_10SEC_INT)
        ])

    def test_should_parse_duration_for_two_users_one_project(self):
        result = get_report_entries_from_json(self.read_api_data('report_two_users_one_project.json'))

        self.assertEqual(result, [
            ReportEntry(PROJECT1, USER1, TIME_5SEC_INT),
            ReportEntry(PROJECT1, USER2, TIME_5SEC_INT)
        ])

    def test_should_parse_duration_for_three_users_three_projects(self):
        result = get_report_entries_from_json(self.read_api_data('report_three_users_three_projects.json'))

        self.assertEqual(result, [
            ReportEntry(PROJECT1, USER1, TIME_5SEC_INT),
            ReportEntry(PROJECT1, USER2, TIME_5SEC_INT),
            ReportEntry(PROJECT2, USER1, TIME_10SEC_INT),
            ReportEntry(PROJECT3, USER2, TIME_3SEC_INT),
            ReportEntry(PROJECT3, USER3, TIME_7SEC_INT),
        ])