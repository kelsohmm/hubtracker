from datetime import datetime, timedelta
from config import API_CONFIG

_ENDPOINT_TEMPLATE = "https://api.hubstaff.com/v1/custom/by_project/team?start_date={0}&end_date={0}"
_USER_TOKEN_HEADER = "Auth-Token"
_APP_TOKEN_HEADER = "App-Token"
_DATE_FORMAT = '%Y-%m-%d'


def build_activity_report_query(requested_date, config=API_CONFIG, now_func=datetime.now):
    if not _is_valid_date_format(requested_date):
        requested_date=_get_yesterday_date(now_func)

    endpoint = _ENDPOINT_TEMPLATE.format(requested_date)
    return endpoint, _build_headers(config)

def _get_yesterday_date(now_func):
    return datetime.strftime(now_func() - timedelta(1), _DATE_FORMAT)

def _is_valid_date_format(requested_date):
    try:
        datetime.strptime(requested_date, _DATE_FORMAT)
        return True
    except:
        return False


def _build_headers(config):
    return {
        _USER_TOKEN_HEADER: str(config.USER_TOKEN),
        _APP_TOKEN_HEADER: str(config.APP_TOKEN),
    }