# 2. Escreva um programa Python para criar uma tupla com números de 1 a 4 e imprima um item 

def create_tuples(quantidade_de_tuplas=1):
    from random import randint
    
    lista_de_tuplas = list()
    
    for i in range(0,quantidade_de_tuplas):        
        a = randint(1,4)
        b = randint(1,4)
        lista_de_tuplas.append((a,b))
    
    return lista_de_tuplas        
        
minhas_tuplas = create_tuples(10)

for tupla in minhas_tuplas:
    print(tupla)