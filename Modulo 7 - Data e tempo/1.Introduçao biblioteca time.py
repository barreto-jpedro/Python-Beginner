import time
# 1. Escreva scripts para mostrar os diversos formatos de tempo conforme se segue: 
# a) Impressão da época padrão 
print(time.gmtime(0))

# b) Segundos que se passaram desde a época 
print(time.time())

# c) Imprime dados do tempo no momento atual 
print(time.ctime())

# d) Cria um objeto time.localtime() e imprime o valor das horas, minutos e segundos 
objeto = time.localtime()
print(time.strftime("%H:%M:%S",objeto))

# e) Imprime se no momento atual estamos em horário de verão ou não 
horarioDeVerao = objeto.tm_isdst

if horarioDeVerao:
    print('Estamos no horario de verao!')
else: 
    print('NAO ESTAMOS no horario de verao!')

