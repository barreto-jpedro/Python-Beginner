# 8. Classe  Bomba  de  Combustível: Faça  um  programa  completo  utilizando  classes  e 
# métodos que: 

# a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos: 
# i. tipoCombustivel. 
# ii. valorLitro 
# iii. quantidadeCombustivel 

class BombaDeCombustível():
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        
    
# b. Possua no mínimo esses métodos: 
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e 
# mostra a quantidade de litros que foi colocada no veículo 
    def abastercerPorValor(self, valor):
        if valor>0:
            quantidade_de_litros = valor / self.valorLitro
            if self.alterarQuantidadeCombustivel(quantidade_de_litros) == True: #valida se ha combustivel suficiente na bomba e altera, se for o caso
                print(f"Foram colocados {quantidade_de_litros} litros de combustivel no veiculo. ")
                self.alterarQuantidadeCombustivel(quantidade_de_litros)
                return True
            else: 
                return False
        else:
            print("ERRO: Insira um valor positivo para abastecer.")
            return False
        
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de 
# combustível e mostra o valor a ser pago pelo cliente. 
    def abastecerPorLitro(self, quantidade_de_litros):
        if self.alterarQuantidadeCombustivel(quantidade_de_litros) == True:
            if quantidade_de_litros>0:            
                valor_final = quantidade_de_litros * self.valorLitro
                print(f"O valor a ser pago eh R${valor_final}")            
                return True
            else:
                print("ERRO: Insira um valor positivo para abastecer.")
                return False
        else:            
            return False
# iii. alterarValor( ) – altera o valor do litro do combustível. 
    def alterarValor(self, novo_valor):                
        if novo_valor == self.valorLitro:
            print("ERRO: O valor antigo e igual ao valor novo. Nada para ser alterado")
            return False               
        else:
            self.valorLitro = novo_valor
            return True
            
# iv. alterarCombustivel( ) – altera o tipo do combustível. 
    def alterarCombustivel(self, novo_tipo):
        if novo_tipo == self.tipoCombustivel:
            print("ERRO: O tipo antigo e igual ao novo tipo. Nada para ser alterado")
            return False               
        else:
            self.tipoCombustivel = novo_tipo
            return True
        
# v. alterarQuantidadeCombustivel(  )  –  altera  a  quantidade  de  combustível restante na bomba. 
    def alterarQuantidadeCombustivel(self, litros_removidos):
        if litros_removidos > self.quantidadeCombustivel:
            print("ERRO: Nao ha combustivel suficiente na bomba para concluir a operacao.")
            return False               
        else:
            self.quantidadeCombustivel -= litros_removidos
            return True
        

# OBS: Sempre que acontecer um abastecimento é necessário atualizar a 
# quantidade de combustível total na bomba. 
 
bombaDeCombustivel = BombaDeCombustível("gasolina",5,100)
bombaDeCombustivel.abastercerPorValor(20)
bombaDeCombustivel.abastecerPorLitro(80)


 