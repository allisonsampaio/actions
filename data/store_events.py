# -*- coding: utf-8 -*-

import os
import json

def write_json(data, filename='data/data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
      
with open('data/data.json') as json_file: 
    data = json.load(json_file) 
    temp = data['lista_eventos'] 
    novo_evento = json.loads(os.environ['GITHUB_CONTEXT'])
    temp.append(novo_evento)
      
write_json(data) 