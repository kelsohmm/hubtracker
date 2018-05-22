import requests
from scraping.activity_report import get_report_entries_from_json
from scraping.activity_table import build_activity_table, EmptyReportError
from scraping.request_building import build_activity_report_query

def request_activity_table(date):
    json = _make_api_request(date)
    report_entries = get_report_entries_from_json(json)
    return build_activity_table(report_entries)


def _make_api_request(date):
    url, headers = build_activity_report_query(date)
    return requests.get(url, headers=headers).text



