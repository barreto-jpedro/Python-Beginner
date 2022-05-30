# 6. Escreva um programa para contar quantos números pares e ímpares existentes entre 1 
# e 10 bem como a soma deles.  
 
# a) usando a instrução while  
par=0
impar=0 
total=0

i = 1
while(i<11):
    if(i%2==0):
        par+=1
    else: 
        impar+=1
    total += i        
    i+=1
    
# b) usando a instrução for e as funções range e sum
par=0
impar=0 
total = []
for i in range(1,11):
    if(i%2==0):
        par+=1
    else: 
        impar+=1
    total.append(i)        

result = sum(total)
