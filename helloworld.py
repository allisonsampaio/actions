# -*- coding: utf-8 -*-
import sys

arquivo = open('file.txt', 'w')
arquivo.writelines(str(sys.argv))

arquivo.close()