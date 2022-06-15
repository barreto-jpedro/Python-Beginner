# 4. Classe Pessoa: Crie uma classe que modele uma pessoa: 
from re import A


class Pessoa():    
# a. Atributos: nome, idade, peso e altura 
    def __init__(self,nome, idade, peso, altura ):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
# b. Métodos:  Envelhercer,  engordar,  emagrecer,  crescer. Obs:  Por  padrão,  a  cada 
# ano  que  nossa  pessoa  envelhece,  sendo  a  idade  dela  menor  que  21  anos,  ela 
# deve crescer 0,5 cm. 
    def envelhecer(self,anos_envelhecidos):
        if self.idade < 21:
            self.crescer(0.5)
        self.idade += anos_envelhecidos
        print(f'Nova idade: {self.idade}')
        return self.idade

    def engordar(self,quilos_engordados):
        self.peso += quilos_engordados
        print(f'Novo peso: {self.peso}')
        return self.peso

    def emagrecer(self,quilos_emagrecidos):
        self.peso += quilos_emagrecidos
        print(f'Novo peso: {self.peso}')
        return self.peso

    def crescer(self,centimetros_aumentados):
        self.altura += centimetros_aumentados
        print(f'Nova altura: {self.altura}')
        return self.altura        


