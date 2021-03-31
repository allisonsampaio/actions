# -*- coding: utf-8 -*-

import os
import json

#with open('events.json') as json_file:
#    data = json.load(json_file)
#    temp = data['events']
#    for event in temp:
        #print(event['sender']['id'])
        #print(event['sender']['login'])
        #print(event['sender']['avatar_url'])
        #print(event['sender']['html_url'])
        #print(event['action'])
        #print(list(event.keys())[1])
        #print('\n')

with open('users.json') as json_users:
    users = json.load(json_users)
    #exist_user = False

    for u in users['users']:
        update_issue(u)
        update_issue_comment(u)
        with open('users.json', 'w') as js:
            json.dump(users, js, indent=4)
        break

#    if(exist_user == False):
#        new_user = {
#            "id": event['sender']['id'],
#            "login": event['sender']['login'],
#            "avatar_url": event['sender']['avatar_url'],
#            "html_url": event['sender']['html_url'],
#            "coins": 1
#        }
#        users['users'].append(new_user)
#        with open('users.json', 'w') as js:
#            json.dump(users, js, indent=4)

def update_issue(user):
    with open('issue.json') as json_file:
        data = json.load(json_file)
        temp = data['events']
        for issue in temp['issue']:
            if user['id'] == issue['sender']['id']:
                user['events']['issue'] += 1
    return user

def update_issue_comment(user):
    with open('issue_comment.json') as json_file:
        data = json.load(json_file)
        temp = data['events']
        for issue_comment in temp['issue_comment']:
            if user['id'] == issue_comment['sender']['id']:
                user['events']['issue_comment'] += 1
    return user
