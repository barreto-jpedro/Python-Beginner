# 1. Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados 
# de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 

def cadastro():
    outro_cadastro = "S"
    todos_os_cadastrados = []
    
    while outro_cadastro == "S":        
        nome = input("Nome: ")
        genero = input("Genero: ")
        idade = int(input("Idade: "))
        
        data = {
            "name": nome,
            "gender": genero,
            "age": idade        
        }
        
        todos_os_cadastrados.append(data)    
        
        outro_cadastro = (input('Outro cadastro? S/N  -> ')).upper()  
        print('\n')  
    
    return todos_os_cadastrados

cadastrados = cadastro()
# a) Quantas pessoas foram cadastradas     
quantidade_de_cadastrados = len(cadastrados)
print(f"Quantidade de cadastrados: {quantidade_de_cadastrados}") 

# b) A média de idade 
soma_das_idade = 0
for pessoa in cadastrados:
    soma_das_idade += pessoa['age'] 

media_das_idades = soma_das_idade/quantidade_de_cadastrados
print(f"Media das idades: {media_das_idades}")

# c) Uma lista com as mulheres 
lista_das_mulheres = list()
for pessoa in cadastrados:
    if pessoa['gender'] == "mulher":
        lista_das_mulheres.append(pessoa['name'])   

print(f"Lista das mulheres: {lista_das_mulheres}")  

# d) Uma lista de pessoas com idade acima da média 
lista_dos_mais_velhos = list()
for pessoa in cadastrados:
    if pessoa['age'] > media_das_idades:
        lista_dos_mais_velhos.append(pessoa['name'])        

print(f"Lista dos mais velhos: {lista_dos_mais_velhos}")  


