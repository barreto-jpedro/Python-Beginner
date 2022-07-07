# importa a biblioteca pandas
import pandas as pd
# armazena os dados da tabela em uma estrutura tipo data frame
df = pd.read_csv("Dados_projeto_modulo_9.csv",sep = ';', encoding="latin-1")
# visualizar alguns dados da tabela carregada
df.head()
print(df.Região.value_counts())
