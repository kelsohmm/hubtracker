from collections import namedtuple

UserKey = namedtuple("UserKey", ["id", "name"])
ProjectKey = namedtuple("ProjectKey", ["id", "name"])
ReportEntry = namedtuple("ReportEntry", ["project", "user", "duration"])