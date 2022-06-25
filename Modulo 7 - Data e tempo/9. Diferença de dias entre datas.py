#9. Faça um programa que calcule a diferença em dias entre antes de ontem e depois de
#amanhã.

from datetime import datetime,timedelta

def numero_de_dias_entre_antes_de_ontem_e_depois_de_amanha():     
        antes_de_ontem = datetime.today()-timedelta(2)
        depois_de_amanha = datetime.today()+timedelta(2)

        quantidade_de_dias = 0

        while antes_de_ontem.day != depois_de_amanha.day:
            antes_de_ontem += timedelta(1)
            quantidade_de_dias+=1
        
        return quantidade_de_dias        
    
print(numero_de_dias_entre_antes_de_ontem_e_depois_de_amanha())
