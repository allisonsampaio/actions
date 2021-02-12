# -*- coding: utf-8 -*-

import os
import json

dados_evento = json.loads(os.environ['GITHUB_CONTEXT'])
filename = "file.json"

with open(filename, "r+") as out_file:
    data = json.load(out_file)
    data.update(dados_evento)
    file.seek(0)
    json.dump(data, out_file, indent=4)

# print(dados_evento["action"])
# print(dados_evento["comment"]["body"])
# print(dados_evento["comment"]["user"]["login"])
