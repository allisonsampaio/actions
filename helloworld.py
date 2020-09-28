# -*- coding: utf-8 -*-
from datetime import datetime
import sys

arquivo = open('file.txt', 'r')
conteudo = arquivo.readlines()
data_e_hora_atuais = datetime.now()
conteudo.append('Action -> ' + data_e_hora_atuais.strftime('%Y-%m-%d %H:%M:%S') + '\n\n')
conteudo.append(str(sys.argv))

arquivo = open('file.txt', 'w')
arquivo.writelines(conteudo)

arquivo.close()