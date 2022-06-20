# 2. Escreva um programa para imprimir uma string "Olá, mundo!" cinco vezes, em que cada 
# uma das impressões demore três segundos entre uma e outra 
from time import sleep

for i in range(0,5):
    print('Hello World!')
    sleep(3)