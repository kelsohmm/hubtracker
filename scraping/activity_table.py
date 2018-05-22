from datetime import timedelta

class EmptyReportError(ValueError):
    pass

def build_activity_table(report_entries, empty_token=" "):
    if len(report_entries) == 0:
        return []

    projects_indexes, users_indexes = _decide_table_header_indexes(report_entries)
    table = _build_zero_filled(empty_token, projects_indexes, users_indexes)
    _fill_cell_values(table, report_entries, projects_indexes, users_indexes)
    return _stringify_durations(table)


def _stringify_durations(table):
    for row in range(1, len(table)):
        for col in range(1, len(table[0])):
            table[row][col] = _to_time_string(table[row][col])
    return table

def _fill_cell_values(table, report_entries, projects_indexes, users_indexes):
    for entry in report_entries:
        row = projects_indexes[entry.project]
        col = users_indexes[entry.user]
        table[row][col] = entry.duration

def _build_zero_filled(empty_token, projects_indexes, users_indexes):
    table = _two_dimensional_list_of_zeros(cols=len(users_indexes.keys()) + 1, rows=len(projects_indexes.keys()) + 1)
    table[0][0] = empty_token

    for user, index in users_indexes.items():
        table[0][index] = user.name

    for project, index in projects_indexes.items():
        table[index][0] = project.name

    return table

def _two_dimensional_list_of_zeros(cols, rows):
    return [[0] * cols for _ in range(rows)]

def _decide_table_header_indexes(report_entries):
    projects_set = {entry.project for entry in report_entries}
    users_set  = {entry.user for entry in report_entries}
    projects_sorted = sorted(projects_set, key=lambda project: project.id)
    users_sorted = sorted(users_set, key=lambda user: user.id)

    return (
        {project: index for index, project in enumerate(projects_sorted, start=1)},
        {user: index for index, user in enumerate(users_sorted, start=1)}
    )

def _to_time_string(duration):
    return str(timedelta(seconds=duration))
