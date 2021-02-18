# -*- coding: utf-8 -*-

import os
import json

with open('data.json') as json_file:
    data = json.load(json_file)
    temp = data['lista_eventos'] 
#    for event in temp:
#        print(event['action'])
#        print(event['sender']['login'])
#        print(event['sender']['avatar_url'])
#        print(event[1])
#        print('\n')

    i = 0
    while(i < len(temp)):
        print(temp[i])
        print('\n\n\n\n')
        i = i + 1