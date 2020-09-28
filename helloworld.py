# -*- coding: utf-8 -*-
import sys
import json

event = sys.argv
arquivo = open('file.json', 'w')
arquivo.writelines(json.loads(event))

arquivo.close()