# -*- coding: utf-8 -*-

import os
import json

dados_evento = json.loads(os.environ['GITHUB_CONTEXT'])
#print(dados_evento)
filename = "file.json"

with open(filename, "w") as out_file:
    json.dump(dados_evento, out_file)

#print(dados_evento["action"])
#print(dados_evento["comment"]["body"])
#print(dados_evento["comment"]["user"]["login"])