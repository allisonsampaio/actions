# -*- coding: utf-8 -*-

import os
import json

dados_evento = json.loads(os.environ['GITHUB_CONTEXT'])

print(dados_evento["action"])
print(str(dados_evento["comment"]["body"]))
print(dados_evento["comment"]["user"]["login"])