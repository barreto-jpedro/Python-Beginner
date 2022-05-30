# 8. Crie um programa que faça a impressão de uma mensagem e a multiplicação de dois 
# números. Utilize módulos e funções para resolução desse problema. 
# a) O usuário deve entrar com a mensagem e com o uso de módulos e funções, essa 
# mensagem deve ser impressa na tela 
def get_and_print_message():
    mensagem = input("Digite uma mensagem para imprimi-la na tela: ")
    print(f"A mensagem digitada foi: {mensagem}")
    
# b) O usuário deve entrar com os valores dos dois multiplicadores e o programa deve exibir 
# o resultado na tela.
def multiplica():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    resultado = a*b
    print(f"O resultado da multiplicacao de {a} por {b} eh: {resultado}")

