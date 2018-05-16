import json

from scraping.types import UserKey, ProjectKey


def parse_users_json(json_string):
    data = json.loads(json_string)
    return {
        'users': read_users_keys(data),
        'projects': read_project_keys(data)
    }

def read_users_keys(data):
    users = set()
    for user in data['users']:
        users.add(UserKey(user['id'], user['name']))
    return users

def read_project_keys(data):
    projects = set()
    for user in data['users']:
        for project in user['projects']:
            projects.add(ProjectKey(project['id'], project['name']))
    return projects
