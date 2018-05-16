import json

from scraping.types import UserKey, ProjectKey


def get_projects(report):
    return report['organizations'][0]['projects']


def get_project_users(project):
    return project['dates'][0]['users']


def parse_reports_json(report_json):
    result = []
    for project in get_projects(json.loads(report_json)):
        project_key = ProjectKey(project['id'], project['name'])

        for user in get_project_users(project):
            user_key = UserKey(user['id'], user['name'])
            result.append((project_key, user_key, user['duration']))

    return result
