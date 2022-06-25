#6. Escreva um programa Python capaz de converter uma string em data e hora.
#• String de exemplo: 01 de janeiro de 2021 13h53
#• Resultado esperado: 2021-01-01 13:53:00
from datetime import datetime

MESES = [
    'Janeiro','Fevereiro','Março','Abril',
    'Maio','Junho','Julho','Agosto',
    'Setembro','Outubro','Novembro','Dezembro'
        ]

def str_to_date_and_time(string_data_e_hora = "01 de Janeiro de 2021 13h53"):
    lista_com_dados = string_data_e_hora.split()
    lista_com_hora_e_minuto = lista_com_dados[-1].split('h')
    
    hora = int(lista_com_hora_e_minuto[0])
    min  = int(lista_com_hora_e_minuto[1])

    dia = int(lista_com_dados[0])

    nome_do_mes = lista_com_dados[2].capitalize()
    numero_do_mes = MESES.index(nome_do_mes)+1

    ano = int(lista_com_dados[4])
    
    
    date = datetime(ano,numero_do_mes,dia,hora,min)
    
    print(date)

str_to_date_and_time()