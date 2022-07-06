# importa a biblioteca pandas
import pandas as pd
# armazena os dados da tabela em uma estrutura tipo data frame
df = pd.read_csv("dadosgovbr---2014.csv",sep = ';', encoding="latin-1")
# visualizar alguns dados da tabela carregada
df.head()
