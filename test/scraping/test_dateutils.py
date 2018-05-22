from unittest import TestCase
from datetime import datetime
from scraping.dateutils import make_valid_date

NOW_DATETIME = datetime(2018, 1, 2)
YESTERDAY_DATE = '2018-01-01'
def now_mock():
    return NOW_DATETIME

class DateutilsTest(TestCase):
    def test_should_return_unchanged_valid_date(self):
        self.assertEqual('2018-02-20', make_valid_date('2018-02-20', now_func=now_mock))
        self.assertEqual('2018-01-01', make_valid_date('2018-01-01', now_func=now_mock))
        self.assertEqual('2016-02-29', make_valid_date('2016-02-29', now_func=now_mock))

    def test_should_return_yesterday_date_when_invalid_date_string(self):
        self.assertEqual(YESTERDAY_DATE, make_valid_date('20180220', now_func=now_mock))
        self.assertEqual(YESTERDAY_DATE, make_valid_date(2018-1-2, now_func=now_mock))
        self.assertEqual(YESTERDAY_DATE, make_valid_date(None, now_func=now_mock))

    def test_should_return_yesterday_date_when_date_not_in_calendar(self):
        self.assertEqual(YESTERDAY_DATE, make_valid_date('2018-12-32', now_func=now_mock))
        self.assertEqual(YESTERDAY_DATE, make_valid_date('2018-02-29', now_func=now_mock))