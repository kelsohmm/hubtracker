

def build_activity_table(report_entries, empty_token=" "):
    [(project, user, duration)] = report_entries

    return [
        [empty_token, user.name],
        [project.name, duration]
    ]


