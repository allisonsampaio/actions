# -*- coding: utf-8 -*-

import os
import json


def write_json(data, filename='data/events.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


novo_evento = json.loads(os.environ['GITHUB_CONTEXT'])

with open('data/events.json') as json_file:
    data = json.load(json_file)
    temp = data['lista_eventos']
    temp.append(novo_evento)
write_json(data)


with open('users.json') as json_users:
    users = json.load(json_users)
    exist_user = False

    for u in users['users']:
        if(u['id'] == novo_evento['sender']['id']):
            u['coins'] = u['coins'] + 1
            exist_user = True
            with open('users.json', 'w') as js:
                json.dump(users, js, indent=4)
            break

    if(exist_user == False):
        new_user = {
            "id": novo_evento['sender']['id'],
            "login": novo_evento['sender']['login'],
            "avatar_url": novo_evento['sender']['avatar_url'],
            "html_url": novo_evento['sender']['html_url'],
            "coins": 1
        }
        users['users'].append(new_user)
        with open('users.json', 'w') as js:
            json.dump(users, js, indent=4)
