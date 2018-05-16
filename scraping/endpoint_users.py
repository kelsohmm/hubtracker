import json

from scraping.types import UserKey


def read_users_keys(data):
    users = set()
    for user in data['users']:
        users.add(UserKey(user['id'], user['name']))
    return users

def parse_users_json(json_string):
    data = json.loads(json_string)
    return {
        'users': read_users_keys(data),
        'projects': set()
    }