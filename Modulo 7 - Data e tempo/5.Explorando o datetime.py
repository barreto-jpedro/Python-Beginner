# 5. Escreva scripts para mostrar os diversos formatos de data e tempo conforme se segue: 
from datetime import datetime

# a) Data e hora atual 
def data_e_hora_atual():
    return datetime.today().strftime('%Y-%m-%d %H:%M')

# b) Ano atual    
def ano_atual():
    return datetime.today().strftime('%Y')

# c) Mês atual 
def mes_atual():
    return datetime.today().strftime('%B')

# d) Número da semana do ano    
def numero_da_semana_do_ano():
    return datetime.today().strftime('%V')
   
# e) Dia atual da semana 
def dia_atual_da_semana():
    return datetime.today().strftime('%A')

# f) Dia do ano 
def dia_do_ano():
    return datetime.today().strftime('%j')

# g) Dia do mês 
def dia_do_mes():
    return datetime.today().strftime('%d')

# h) Dia da semana 
def dia_da_semana():
    return datetime.today().strftime('%w')


#A    
print( f"Data e hora atual: {data_e_hora_atual()}")

#B
print( f"Ano atual: {ano_atual()}")

#C
print( f"Mes atual: {mes_atual()}")

#D
print( f"Numero da semana do ano: {numero_da_semana_do_ano()}")

#E
print( f"Dia atual da semana: {dia_atual_da_semana()}")

#F
print( f"Dia do ano: {dia_do_ano()}")

#G
print( f"Dia do mes: {dia_do_mes()}")

#H
print( f"Dia da semana: {dia_da_semana()}")