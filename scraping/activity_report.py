import json

from scraping.types import UserKey, ProjectKey, ReportEntry


def get_report_entries_from_json(report_json):
    result = []
    for project in _get_projects(json.loads(report_json)):
        project_key = ProjectKey(project['id'], project['name'])

        for user in _get_project_users(project):
            user_key = UserKey(user['id'], user['name'])
            result.append(ReportEntry(project_key, user_key, user['duration']))

    return result

def _get_projects(report):
    return report['organizations'][0]['projects']

def _get_project_users(project):
    return project['dates'][0]['users']