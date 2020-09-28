# -*- coding: utf-8 -*-
import sys

event = sys.argv
arquivo = open('file.json', 'w')
arquivo.writelines(event)

arquivo.close()