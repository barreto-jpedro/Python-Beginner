# 6. Classe  Conta  Corrente: Crie  uma  classe  para  implementar  uma  conta  corrente.  
class contaCorrente():
    def __init__(self,numero_da_conta,nome_do_correntista,saldoInicial=0):
# A classe  deve  possuir  os  seguintes  atributos:  número  da  conta,  nome  do  correntista  e saldo.
        self.numero_da_conta = numero_da_conta
        self.nome_do_correntista = nome_do_correntista
        self.saldo = saldoInicial
        
#  Os  métodos  são  os  seguintes:  alterarNome,  depósito  e  saque;  No  construtor, 
# saldo é opcional, com valor default zero e os demais atributos são obrigatórios.        

    def alterarNome(self,novo_nome):
        nome_antigo = self.nome_do_correntista
        if nome_antigo != novo_nome:               
            self.nome = novo_nome
            print(f"O nome foi alterado de {nome_antigo} para {novo_nome}")
            return True
        else:
            print("Nao ha nada para ser alterado.")
            return False
    def deposito(self,dinheiro):
        self.saldo += dinheiro
        print(f'O novo saldo eh {self.saldo}')
        return True
    
    def saque(self,dinheiro):
        if self.saldo >= dinheiro:
            self.saldo -= dinheiro
            print(f'O novo saldo eh {self.saldo}')
            return True
        else:
            print('Saldo insuficiente.')
            return False

minhaconta = contaCorrente(14,"Joao")
minhaconta.alterarNome("Joao Pedro")
minhaconta.deposito(100)
minhaconta.saque(30)