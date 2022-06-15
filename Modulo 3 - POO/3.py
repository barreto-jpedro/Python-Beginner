# 3. Classe Retangulo: Crie uma classe que modele um retangulo: 
class Retangulo():    
# a. Atributos:  LadoA,  LadoB  (ou  Comprimento  e  Largura,  ou  Base  e  Altura,  a 
# escolher) 
    def __init__(self,comprimento,largura):
        self.comprimento = comprimento
        self.largura = largura
        
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular 
# Perímetro; 
    def mudar_valor_dos_lados(self, dimensao):
        comprimento, largura = dimensao
        self.comprimento = comprimento
        self.largura = largura        
    
    def get_valor_dos_lados(self):
        print(f"O tamanho do comprimento eh: {self.comprimento}")
        print(f"O tamanho da largura eh: {self.largura}")
        return (self.comprimento, self.largura)
    
    def area(self):
        area = self.comprimento * self.largura
        return area
    
    def perimetro(self):
        perimetro = 2 * (self.comprimento + self.largura)
        return perimetro
    
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe 
# as  medidades  de  um  local.  Depois,  deve  criar  um  objeto  com  as  medidas  e 
# calcular a quantidade de pisos e de rodapés necessárias para o local. 

comprimento = float(input("Digite o comprimento do local: "))
largura = float(input("Digite a largura do local: "))

local = Retangulo(comprimento,largura)
area = local.area()
perimetro = local.perimetro()

print(f'Voce precisara de {area}m² de piso e {perimetro}m de rodape!')

# Testes
# lados = local.get_valor_dos_lados()
# print(lados)
# novo_comprimento = 3
# nova_largura = 2
# local.mudar_valor_dos_lados((novo_comprimento,nova_largura))
# local.get_valor_dos_lados()
