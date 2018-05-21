from unittest import TestCase

from datetime import datetime

from scraping.api_request import build_activity_report_query


class TEST_CONFIG:
    APP_TOKEN="XYZ"
    USER_TOKEN="ZYX"
    ORGANIZATION_ID=111

TEST_CONFIG_HEADERS = {
    "Auth-Token": "XYZ",
    "App-Token": "ZYX",
    "organizations": [111],
}

def now_mock():
    return datetime(2018, 1, 2)


class ApiRequestBuildingTest(TestCase):
    def test_should_build_request_with_headers_for_valid_date_string(self):
        endpoint, headers = build_activity_report_query('2018-01-03', config=TEST_CONFIG, now_func=now_mock)

        self.assertEqual(endpoint, "https://api.hubstaff.com/v1/custom/by_date/team?start_date=2018-01-03&end_date=2018-01-03")
        self.assertEqual(headers, TEST_CONFIG_HEADERS)

    def test_should_use_yesterday_date_when_date_empty(self):
        endpoint, headers = build_activity_report_query(config=TEST_CONFIG, now_func=now_mock)

        self.assertEqual(endpoint, "https://api.hubstaff.com/v1/custom/by_date/team?start_date=2018-01-01&end_date=2018-01-01")
        self.assertEqual(headers, TEST_CONFIG_HEADERS)