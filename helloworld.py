from datetime import datetime

arquivo = open('file.txt', 'r')
conteudo = arquivo.readlines()
data_e_hora_atuais = datetime.now()
conteudo.append('Action -> ' + data_e_hora_atuais.strftime('%Y-%m-%d %H:%M:%S') + '\n')

arquivo = open('file.txt', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()