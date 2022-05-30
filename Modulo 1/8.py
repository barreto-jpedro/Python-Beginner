# 8. Vamos reescrever o programa acima criando uma função bhaskara que recebe como 
# parâmetros os coeficientes a, b e c e retorna as raízes da equação.  
 
# Dica: Iremos aprender sobre funções no próximo módulo, fique tranquilo. Contudo, você já 
# pode começar a praticar. A definição da função é a seguinte: 
 
#    def bhaskara(a, b, c): 
#    delta = b ** 2 - 4 * a * c 
#    if delta < 0: 
# mentorama.  
 
#        return None 
#     else: 
#         raizes = [] 
#         m1 = math.sqrt(delta) 
#         r1 =(-b + m1) / (2 * a) 
#         raizes.append(r1) 
#         r2 =(-b - m1) / (2 * a) 
#         raizes.append(r2) 
#         return raizes 
 
#        Responda as questões a seguir: 
# a) O que significam palavras reservadas em Python? Quais são as palavras reservadas no 
# código acima? 
    Palavras reservadas sao as palavras que o python separa para executarem açao no codigo.
    No codigo acima, as palavras reservadas sao: def, if, return, else e append.
    
# b)  Qual a função de cada uma dessas palavras reservadas no código? 
    def-> definir uma funçao
    if, else-> criar uma condiçao no fluxo do programa
    return-> retornar algo(valor, outra funçao, nada, ...) da funçao     
    append-> adicionar algo em uma lista
    
# c) Implemente a função acima e mostre na tela, o resultado da equação de segundo grau. 

import math
def bhaskara(a, b, c): 
    delta = b ** 2 - 4 * a * c 
    if delta < 0:  
        return None 
    else: 
        raizes = [] 
        m1 = math.sqrt(delta) 
        r1 =(-b + m1) / (2 * a) 
        raizes.append(r1) 
        r2 =(-b - m1) / (2 * a) 
        raizes.append(r2) 
    return raizes 

print(bhaskara(1 ,-5 ,4))

    