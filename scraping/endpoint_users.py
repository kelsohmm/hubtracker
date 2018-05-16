import json

from scraping.types import UserKey, ProjectKey


def parse_users_json(json_string):
    data = json.loads(json_string)
    return {
        'users': read_users_keys(data),
        'projects': read_project_keys(data)
    }

def read_users_keys(data):
    users = dict()
    for user in data['users']:
        users[user['id']] = user['name']
    return {
        UserKey(id, name) for id, name in users.items()
    }

def read_project_keys(data):
    projects = dict()
    for user in data['users']:
        for project in user['projects']:
            projects[project['id']] = project['name']
    return {
        ProjectKey(id, name) for id, name in projects.items()
    }
