# 7. Escreva um programa para resolver equações do segundo grau representadas por 
# ax2+bx+c usando a Fórmula de Bhaskara.  
 
# a) sem usar o módulo math  
def bhaskara_sem_o_math(a,b,c):
    delta = b*b-4*a*c  
    if delta<0:
        return('O resultado e complexo!')
    primeira_raiz = round((-b+(delta)**(1/2))/2*a,2)
    segunda_raiz = round((-b-(delta)**(1/2))/2*a,2)
    return primeira_raiz, segunda_raiz

# b) usando o módulo math  
def bhaskara_com_o_math(a,b,c):
    import math
    delta = math.pow(b,2)-4*a*c  
    if delta<0:
        return('O resultado e complexo!')
    primeira_raiz = round((-b+math.pow(delta,0.5))/2*a,2)
    segunda_raiz  = round((-b-math.pow(delta,0.5))/2*a,2)
    return primeira_raiz, segunda_raiz

# c)Teste seu programa com os coeficientes:  
# a=1,b=-5,c=6  
print(bhaskara_sem_o_math(1,-5,6))
print(bhaskara_com_o_math(1,-5,6))

# a=1,b=0,c=-9  
print(bhaskara_sem_o_math(1,0,-9))
print(bhaskara_com_o_math(1,0,-9))

# a=5,b=-45,c=0  
print(bhaskara_sem_o_math(5,-45,0))
print(bhaskara_com_o_math(5,-45,0))

# a=1,b=-1,c=-12  
print(bhaskara_sem_o_math(1,-1,-12))
print(bhaskara_com_o_math(1,-1,-12))

# a=1,b=-6,c=10  
print(bhaskara_sem_o_math(1,-6,10))
print(bhaskara_com_o_math(1,-6,10))
 
# Dica: Você não precisa necessariamente fazer uma entrada dos valores de a, b e c a partir 
# do usuário. Você pode declarar esses valores antes e efetuar o cálculo. 
 
# Dica 2: Para importar o módulo math, use o comando import math, assim você poderá 
# usar com mais facilidade funções matemáticas da biblioteca. Para saber mais detalhes, 
# consulte: https://docs.python.org/pt-br/3/library/math.html 
 
 
 
 
 