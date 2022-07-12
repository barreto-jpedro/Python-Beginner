import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Dados_projeto_modulo_9.csv",sep = ';', encoding="latin-1")

#5. Gere um gráfico com titulo, nome dos eixos, cor e legenda para as seguintes situações:
#a) Frequência de reclamações por sexo
titulo_do_grafico = "Frequência de reclamações por sexo"
titulo_eixo_x = "Sexo"
titulo_eixo_y = "Frequencia"
titulos_barras = ["Masc.","Fem."]
dados = df.Sexo.value_counts().to_list()

plt.bar(titulos_barras, dados, color="red")
plt.xticks(titulos_barras)
plt.ylabel(titulo_eixo_y)
plt.xlabel(titulo_eixo_x)
plt.title(titulo_do_grafico)
plt.show()

#* b) Frequencia de reclamações por estado
titulo_do_grafico = "Frequência de reclamações por estado"
titulo_eixo_x = "Estados"
titulo_eixo_y = "Frequencia"
titulos_barras = ["SE","S","NE","CO","N"]
dados = df.Região.value_counts().to_list()

plt.bar(titulos_barras, dados, color="blue")
plt.xticks(titulos_barras)
plt.ylabel(titulo_eixo_y)
plt.xlabel(titulo_eixo_x)
plt.title(titulo_do_grafico)
plt.show()

#* c) Frequência de reclamações respondidas e não respondidas
titulo_do_grafico = "Frequência de reclamações respondidas e não respondidas"
titulo_eixo_x = "Reclamações"
titulo_eixo_y = "Frequencia"
titulos_barras = ["Respondidas","Não respondida"]
dados = df.Respondida.value_counts().to_list()

plt.bar(titulos_barras, dados, color="green")
plt.xticks(titulos_barras)
plt.ylabel(titulo_eixo_y)
plt.xlabel(titulo_eixo_x)
plt.title(titulo_do_grafico)
plt.show()

