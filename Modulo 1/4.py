# Escreva um programa que leia dois números e que pergunte qual operação você deseja
# realizar. Você deve poder calcular a soma (+), subtração(-), multiplicação(*) e divisão(/).
# Exiba o resultado da operação.
a = int(input('a: '))
b = int(input('b: '))

operation = input('Qual operaçao voce quer realizar? (+, -, *, /) -> ')

if operation == '+':
    result = a + b

if operation == '-':
    result = a - b
    
if operation == '*':
    result = a * b
    
if operation == '/':    
    result = a / b    


print(f'Result: {result}')