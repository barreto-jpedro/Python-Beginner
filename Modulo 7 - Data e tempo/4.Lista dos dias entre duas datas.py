# 4. Escreva um programa para obter uma lista de datas entre duas datas. Considere o passo de 
# um dia e reproduza o intervalo das datas entre 16/10/87 e 25/10/87 

from datetime import datetime, timedelta

def dias_entre_as_datas(firstDay, lastDay):     
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
        
        datas_entre_as_duas_datas = list()
        
        while first_day != last_Day:
            datas_entre_as_duas_datas.append(first_day.strftime("%d/%m/%Y"))
            first_day += timedelta(1)
        
        return datas_entre_as_duas_datas        
    
        
for day in dias_entre_as_datas("16/10/1987" , "25/10/1987" ):
    print(day)