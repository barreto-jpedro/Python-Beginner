 
# 9.  Considerando a string s = 'Mentorama' escreva um programa que:  
# a) converta a string para maiúsculo, em seguida  
s = 'Mentorama'

def maiusculo(palavra):    
    return palavra.upper()
    
# b) imprima-a de trás para frente  
def ao_contrario(palavra):    
    print(palavra[::-1])
    
# c) imprima somente as vogais
def apenas_vogais(palavra):
    for i in palavra:
        if i in ["a","b","c","d","e"]:
            print(i)

