from datetime import timedelta


def build_activity_table(report_entries, empty_token=" "):
    [only_entry] = report_entries

    return [
        [empty_token, only_entry.user.name],
        [only_entry.project.name, to_time_string(only_entry.duration)]
    ]

def to_time_string(duration):
    return str(timedelta(seconds=duration))
