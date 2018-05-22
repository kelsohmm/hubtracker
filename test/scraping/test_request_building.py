from unittest import TestCase
from scraping.request_building import build_activity_report_query


class TEST_CONFIG:
    APP_TOKEN="XYZ"
    USER_TOKEN="ZYX"

TEST_CONFIG_HEADERS = {
    "Auth-Token": "ZYX",
    "App-Token": "XYZ",
}


class ApiRequestBuildingTest(TestCase):
    def test_should_build_request_with_headers_for_valid_date_string(self):
        endpoint, headers = build_activity_report_query('2018-01-03', config=TEST_CONFIG)

        self.assertEqual(endpoint, "https://api.hubstaff.com/v1/custom/by_project/team?start_date=2018-01-03&end_date=2018-01-03")
        self.assertEqual(headers, TEST_CONFIG_HEADERS)
