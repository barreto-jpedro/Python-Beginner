# 2. Classe Quadrado: Crie uma classe que modele um quadrado: 
class Quadrado():
# a. Atributos: Tamanho do lado 
    def __init__(self,tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;        
    def muda_valor_do_lado(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado
    
    def get_lado(self):
        print(f"O tamanho do lado eh: {self.tamanho_do_lado}")
        return self.tamanho_do_lado

    def calcula_area(self):
        area = self.tamanho_do_lado ** 2  
        print(f"A area do quadrado eh: {area}")
        return area

# Testes
# meu_quadrado = Quadrado(2)
# print(meu_quadrado.tamanho_do_lado)
# meu_quadrado.muda_valor_do_lado(4)
# print(meu_quadrado.tamanho_do_lado)
# lado = meu_quadrado.get_lado()
# print(lado)
# print(meu_quadrado.calcula_area())