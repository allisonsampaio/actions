# -*- coding: utf-8 -*-

import os
import json

def update_issue(user):
    with open('data/issue.json') as json_file:
        data = json.load(json_file)
        temp = data['issue']
        user['events']['issue'] = 0
        for issue in temp:
            if user['id'] == issue['sender']['id']:
                user['events']['issue'] += 1
    return user

def update_issue_comment(user):
    with open('data/issue_comment.json') as json_file:
        data = json.load(json_file)
        temp = data['issue_comment']
        user['events']['issue_comment'] = 0
        for issue_comment in temp:
            if user['id'] == issue_comment['sender']['id']:
                user['events']['issue_comment'] += 1
    return user

with open('data/users.json') as json_users:
    users = json.load(json_users)
    #exist_user = False

    for u in users['users']:
        update_issue(u)
        update_issue_comment(u)
        with open('data/users.json', 'w') as js:
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
