# -*- coding: utf-8 -*-

import os
import json

with open('events.json') as json_file:
    data = json.load(json_file)
    temp = data['events']
    for event in temp:
        #print(event['sender']['id'])
        #print(event['sender']['login'])
        #print(event['sender']['avatar_url'])
        #print(event['sender']['html_url'])
        #print(event['action'])
        #print(list(event.keys())[1])
        #print('\n')

        with open('users.json') as json_users:
            users = json.load(json_users)
            exist_user = False

            for u in users['users']:
                if(u['id'] == event['sender']['id']):
                    u['coins'] = u['coins'] + 1
                    exist_user = True
                    with open('users.json', 'w') as js:
                        json.dump(users, js, indent=4)
                    break

            if(exist_user == False):
                new_user = {
                    "id": event['sender']['id'],
                    "login": event['sender']['login'],
                    "avatar_url": event['sender']['avatar_url'],
                    "html_url": event['sender']['html_url'],
                    "coins": 1
                }
                users['users'].append(new_user)
                with open('users.json', 'w') as js:
                    json.dump(users, js, indent=4)
