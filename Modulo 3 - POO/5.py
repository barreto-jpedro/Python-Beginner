# 5. Crie um programa que tenha uma classe Carro. Este programa deve ter no mínimo 3 
# propriedades para a classe carro e no mínimo 3 métodos para ela, sendo um destes 
# métodos para imprimir todos os dados de um carro. 
class carro():
    def __init__(self,cor, quilometragem, combustivel):
        self.cor = cor
        self.quilometragem = quilometragem
        self.combustivel = combustivel
        
    def mudaCor(self, nova_cor):
        self.cor = nova_cor
        print(f"Nova cor: {self.cor}")
        return (f'A cor do carro foi alterada com sucesso para {nova_cor}')
    
    def abastecer(self, combustivel):
        if self.combustivel == 100:
            return "O carro ja esta abastecido!"
        else:
            self.abastecer = combustivel
            return "O carro foi abastecido com sucesso."
    
    def revisao(self):
        if self.quilometragem > 100000:
            return "Esta na hora de mandar para a revisao..."
        else:
            return "Ainda NAO e' necessario mandar para a revisao..."
        
# a. Crie 3 objetos para carros diferentes que recebem como entrada os parâmetros 
# das propriedades que você definiu 
corola = carro("prata", 150000, 70)
ideia = carro("branco", 70000, 50)
celta = carro("preto", 50000, 20)

# b. Consulte cada um desses parâmetros para cada um dos objetos criados no 
# exercício anterior 
print(corola.cor)
print(corola.quilometragem)
print(corola.combustivel)

print(celta.cor)
print(celta.quilometragem)
print(celta.combustivel)

print(ideia.cor)
print(ideia.quilometragem)
print(ideia.combustivel)

# c. Chame cada um dos métodos criados para verificar o correto funcionamento
corola.mudaCor("preto")
print(celta.abastecer("100"))
print(ideia.revisao())

