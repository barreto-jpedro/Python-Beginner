# 4. Crie 3 conjuntos conforme estrutura a seguir: 
setx = set(["apple", "mango"]) 
sety = set(["mango", "orange"]) 
setz = set(["mango"]) 
 
# Faça as seguintes operações sobre conjuntos: 
# a) Faça a união dos três conjuntos e imprima o resultado 
set_global = setx | sety | setz
print(set_global)

# b) Verifique quais os elementos comuns do conjunto setx e sety e imprima o resultado 
set_global = setx & sety & setz
print(set_global)


# c) Verifique se o conjunto setx é subconjunto do conjunto sety e setz utilizando issubset()  
print(setx.issubset(sety))
print(setx.issubset(setz))

# d) Verifique quais elementos do conjunto setx não existem em sety
print(setx - sety)