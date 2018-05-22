from datetime import datetime, timedelta

_DATE_FORMAT = '%Y-%m-%d'


def make_valid_date(date_str, now_func=datetime.now):
    return date_str if _is_valid_date_format(date_str) \
          else _get_yesterday_date(now_func)

def _get_yesterday_date(now_func):
    return datetime.strftime(now_func() - timedelta(1), _DATE_FORMAT)

def _is_valid_date_format(requested_date):
    try:
        datetime.strptime(requested_date, _DATE_FORMAT)
        return True
    except:
        return False