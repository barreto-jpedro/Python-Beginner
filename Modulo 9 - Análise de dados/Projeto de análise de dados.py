# importa a biblioteca pandas
import pandas as pd

# armazena os dados da tabela em uma estrutura tipo data frame
df = pd.read_csv("Dados_projeto_modulo_9.csv",sep = ';', encoding="latin-1")

# visualizar alguns dados da tabela carregada
print()
print(df.head())
print(df.Região.value_counts())
print()

#Qual a quantidade de reclamações registradas?
print()
quantidade_de_linhas = len(df.index)
print("quantidade_de_linhas: ",quantidade_de_linhas)
print()

#Qual é o tempo médio, máximo e mínimo de resposta?
print()
tempo_maximo = df["Tempo Resposta"].max()
print("Tempo_maximo: ",tempo_maximo)

tempo_minimo = df["Tempo Resposta"].min()
print("tempo_minimo: ",tempo_minimo)

tempo_medio = df["Tempo Resposta"].mean()
print("tempo_medio: ",tempo_medio)
print()

#Qual é a nota média, máxima e mínima do consumidor?
print()
nota_maxima = df["Nota do Consumidor"].max()
print("nota_maxima: ",nota_maxima)

nota_minima = df["Nota do Consumidor"].min()
print("nota_minima: ",nota_minima)

nota_media = df["Nota do Consumidor"].mean()
print("nota_media: ",nota_media)
print()

#Como podemos correlacionar a nota do consumidor com o tempo de resposta? Explique.
not_related = 0
related = 0
total = 0

for (nota, tempo) in zip(df["Nota do Consumidor"], df["Tempo Resposta"]) :
    if nota > nota_media and tempo < tempo_medio:
        related+=1
    
    elif nota < nota_media and tempo > tempo_medio:
        related+=1
    
    elif nota < nota_media and tempo < tempo_medio:
        not_related+=1
    
    elif nota > nota_media and tempo > tempo_medio:
        not_related+=1
    
    total+=1

percetage_related = related/total
percetage_not_related = not_related/total


print("related",percetage_related)
print("not_related",percetage_not_related)

#Qual a quantidade de reclamações por Sexo?

#Qual a quantidade de reclamações por Estado?

#Qual é a porcentagem de reclamações registradas e não respondidas?