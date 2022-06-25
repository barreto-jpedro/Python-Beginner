#7. Escreva um programa Python para subtrair 8 dias da data atual.
#• Data atual: 25/01/2021
#• Data esperada: 17/01/2021

from datetime import datetime, timedelta 

def subtrair_datas(firstDay='25/01/2021', amount_to_be_subtracted=8):     
        firstDay = firstDay.split('/')
                
        dia = int(firstDay[0])
        mes = int(firstDay[1])
        ano = int(firstDay[2])        
        first_day = datetime(ano,mes,dia)
        
        for i in range(0,amount_to_be_subtracted):
            first_day -= timedelta(1)
        
        dia = str(first_day.day)
        mes = str(first_day.month)
        ano = str(first_day.year)        
        

        date = dia+'/'+mes+'/'+ano
        
        return date         

print(subtrair_datas())