#Importa a biblioteca pandas
import pandas as pd

#Armazena os dados da tabela em uma estrutura tipo data frame
df = pd.read_csv("Dados_projeto_modulo_9.csv",sep = ';', encoding="latin-1")

#Visualizar alguns dados da tabela carregada
print(df.head())

#Qual a quantidade de reclamações registradas?
print()
quantidade_de_reclamacoes = len(df.index)
print("Quantidade de reclamações registradas: ",quantidade_de_reclamacoes)

#Qual é o tempo médio, máximo e mínimo de resposta?
print()
tempo_maximo = df["Tempo Resposta"].max()
print("Tempo_maximo: ",tempo_maximo)

tempo_minimo = df["Tempo Resposta"].min()
print("tempo_minimo: ",tempo_minimo)

tempo_medio = df["Tempo Resposta"].mean()
print("tempo_medio: ",tempo_medio)

#Qual é a nota média, máxima e mínima do consumidor?
print()
nota_maxima = df["Nota do Consumidor"].max()
print("nota_maxima: ",nota_maxima)

nota_minima = df["Nota do Consumidor"].min()
print("nota_minima: ",nota_minima)

nota_media = df["Nota do Consumidor"].mean()
print("nota_media: ",nota_media)

#Como podemos correlacionar a nota do consumidor com o tempo de resposta? Explique.
inversamente_proporcional = 0
diretamente_proporcional = 0

for (nota, tempo) in zip(df["Nota do Consumidor"], df["Tempo Resposta"]) :
    #Nota alta e o tempo baixo - Inversamente proporcional
    if nota > nota_media and tempo < tempo_medio:
        inversamente_proporcional+=1
    
    #Nota baixa e o tempo alto - Inversamente proporcional
    elif nota < nota_media and tempo > tempo_medio:
        inversamente_proporcional+=1
    
    #Nota baixa e o tempo baixo - Diretamente proporcional
    elif nota < nota_media and tempo < tempo_medio:
        diretamente_proporcional+=1

    #Nota alta e o tempo alto - Diretamente proporcional
    elif nota > nota_media and tempo > tempo_medio:
        diretamente_proporcional+=1

if diretamente_proporcional > 2 * inversamente_proporcional: 
    print("As grandezas são DIRETAMENTE proporcionais. ")

elif inversamente_proporcional > 2 * diretamente_proporcional:
    print("As grandezas são INVERSAMENTE proporcionais. ")

else:
    print("Os dados são inconclusivos para estabelecer uma relação entre as grandezas.")

#Qual a quantidade de reclamações por Sexo?
print(f"Quantidade de reclamações por Sexo: {df.Sexo.value_counts()}")

#Qual a quantidade de reclamações por Estado?
print(f"Quantidade de reclamações por Estado: {df.Região.value_counts()}")

#Qual é a porcentagem de reclamações registradas e não respondidas?
total = df.Total.value_counts().to_list()[0]
nao_respondidas = df.Respondida.value_counts().to_list()[1]
porcentagem_nao_respondida = (1-nao_respondidas/total)*100

print(f"A porcentagem de reclamações registradas e não respondidas eh: {porcentagem_nao_respondida}%")