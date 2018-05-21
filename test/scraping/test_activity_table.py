from collections import namedtuple
from unittest import TestCase

from scraping.types import ReportEntry
from test.scraping.data_common import *
from scraping.activity_table import build_activity_table

EMPTY=" "
ActivityTableTestData = namedtuple("ActivityTableTestData", ["input", "output"])

SINGLE_ENTRY = ActivityTableTestData(
    input=[
ReportEntry(PROJECT1, USER1, TIME_10SEC_INT)
    ],output=[
[EMPTY         , USER1_NAME] ,
[PROJECT1_NAME , TIME_10SEC_STR]
    ])

class ReportsParsingTest(TestCase):
    def _run_test_for(self, test_data):
        self.assertEqual(test_data.output, build_activity_table(test_data.input, empty_token=EMPTY))

    def test_should_build_2_dim_table_for_single_entry(self):
        self._run_test_for(SINGLE_ENTRY)

