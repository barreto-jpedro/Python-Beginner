# 1. Classe Bola: Crie uma classe que modele uma bola: 
# a. Atributos: Cor, circunferência, material 
class Bola():
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

# b. Métodos: trocaCor e mostraCor
    def trocaCor(self, cor):
        self.cor = cor
        
    
    def mostraCor(self):
        print(f'A cor da bola eh: {self.cor}')
        return self.cor

# Teste
# minha_bola = Bola('verde','35cm','borracha')
# minha_bola.mostraCor()
# minha_bola.trocaCor('vermelho')
# minha_bola.mostraCor()
