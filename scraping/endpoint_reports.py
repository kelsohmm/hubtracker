import json

from scraping.types import UserKey, ProjectKey


def parse_reports_json(json_string):
    data = json.loads(json_string)
    return {}
