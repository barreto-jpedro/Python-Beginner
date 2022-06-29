from threading import Thread
import threading 
from time import sleep 
#2.  Crie  duas  funções,  proc1  e  proc2  que  imprime  a  mensagem  "Processo  1"  e  "Processo  2" 
#respectivamente e siga as instruções: 
def imprime_mensagem_1(mensagem="Processo 1"):
    sleep(5) #c)
    print(f"A mensagem é: {mensagem}")

def imprime_mensagem_2(mensagem="Processo 2"):
    sleep(30) #c)
    print(f"A mensagem é: {mensagem}")

#a) Inicialize as funções a partir de um objeto Thread t1 e t2 respectivamente 
thread_1 = Thread(target=imprime_mensagem_1)
thread_1.start()

thread_2 = Thread(target=imprime_mensagem_2)
thread_2.start()

#b) Consulte se os objetos criados estão ativos 
if thread_1.is_alive():
    print("O objeto thread criado está ativo")

if thread_2.is_alive():
    print("O objeto thread criado está ativo")
   
#c) Importe o modulo time e crie um delay de tempo em cada uma das funções, sendo sleep 
#5 e 30 segundos em proc1 e proc2 respectivamente 

# FEITO 

#d) Consulte rapidamente (antes de 30 segundos) se cada um dos objetos thread está ativo 
#e imprima na tela

if thread_1.is_alive():
    print("O objeto thread criado está ativo")

if thread_2.is_alive():
    print("O objeto thread criado está ativo")
