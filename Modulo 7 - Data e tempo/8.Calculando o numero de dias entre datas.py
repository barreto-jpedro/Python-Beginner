#8. Escreva um programa Python para calcular o número de dias entre dois datetimes. 
#   A diferença entre os dias deve ser igual a 10.

from datetime import datetime,timedelta

def numero_de_dias_entre_as_datas(firstDay, lastDay):     
        firstDay = firstDay.split('/')
        lastDay = lastDay.split('/')
                
        dia = int(firstDay[0])
        mes = int(firstDay[1])
        ano = int(firstDay[2])        
        first_day = datetime(ano,mes,dia)
        
        dia = int(lastDay[0])
        mes = int(lastDay[1])
        ano = int(lastDay[2])        
        last_Day = datetime(ano,mes,dia)
                
        quantidade_de_dias = 0

        while first_day != last_Day:
            first_day += timedelta(1)
            quantidade_de_dias+=1
        
        return quantidade_de_dias        
    
print(numero_de_dias_entre_as_datas("16/10/1987" , "26/10/1987" ))
