from config import API_CONFIG

_ENDPOINT_TEMPLATE = "https://api.hubstaff.com/v1/custom/by_project/team?start_date={0}&end_date={0}"
_USER_TOKEN_HEADER = "Auth-Token"
_APP_TOKEN_HEADER = "App-Token"


def build_activity_report_query(requested_date, config=API_CONFIG):
    endpoint = _ENDPOINT_TEMPLATE.format(requested_date)
    return endpoint, _build_headers(config)

def _build_headers(config):
    return {
        _USER_TOKEN_HEADER: str(config.USER_TOKEN),
        _APP_TOKEN_HEADER: str(config.APP_TOKEN),
    }