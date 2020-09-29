# -*- coding: utf-8 -*-

import os
dados_evento = os.environ['GITHUB_CONTEXT']

print(dados_evento['action'])
print(dados_evento['comment']['body'])
print(dados_evento['comment']['user']['login'])