# 7. Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O 
# usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se  de  que  o  número  do  canal  e  o  nível  do  volume  permanecem  dentro  de 
# faixas válidas

class TV():
    def __init__(self,canal_atual,volume_atual):
        self.canal = canal_atual
        self.volume = volume_atual
    
    def trocarCanal(self,novo_canal):
        if novo_canal > 100 or novo_canal < 1:
            print(f"O canal solicitado esta fora das faixas validas")
            return False        
        else: 
            self.canal = novo_canal
            print(f"Novo canal: {self.canal}")
            return True
    def trocaVolume(self,novo_volume):
        if novo_volume > 5 or novo_volume < 0:
            print(f"O volume solicitado esta fora das faixas validas")
            return False        
        else: 
            self.volume = novo_volume
            print(f"Novo volume: {self.volume}")
            return True            

minhaTV = TV(20,4)            
minhaTV.trocaVolume(5)
minhaTV.trocarCanal(100)