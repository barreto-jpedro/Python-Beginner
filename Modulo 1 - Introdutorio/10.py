# 10. Escreva um programa que receba como entrada do usuário o nome “João” 
# sobrenome “da Silva”, idade “25”, Cidade “São Paulo”, ddd “11”, telefone “3333-3333” e 
# faça as seguintes instruções: 
 
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")
ddd = int(input("Ddd: "))
telefone = int(input("Telefone: "))
 
# a) imprima na tela o nome completo em uma única linha  
# Nome: João da Silva 
print(f'Nome completo: {nome} {sobrenome}')
 
# b) imprima na tela o telefone com ddd em uma única linha  
# Telefone: (11)3333-3333 
print(f'Telefone: ({ddd}){telefone}')
 
# c) Imprima na tela a idade 
# Idade: 25 
print('Idade: ',idade)
 
# d) Imprima na tela a cidade  
# Cidade: São Paulo 
print('Cidade: ',cidade)