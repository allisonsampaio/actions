# -*- coding: utf-8 -*-
import sys

arquivo = open('file.txt', 'w')
event = sys.argv

arquivo.writelines(event.comment.body)

arquivo.close()