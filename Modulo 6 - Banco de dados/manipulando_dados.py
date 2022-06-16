import sqlite3
DB = sqlite3.connect('dataBase.db')
cursor = DB.cursor()
cursor.execute(""" CREATE TABLE Funcionarios(
    Codigo integer, 
    PrimeiroNome text,
    SegundoNome	text,
    UltimoNome	text,
    DataNasci	text,
    CPF	integer,
    RG	integer,
    Endereco	text,
    CEP	integer,
    Cidade	text,
    Fone	integer,
    CodigoDepartamento	integer,
    Funcao	text,
    Salario	REAL,
    PRIMARY KEY("Codigo")
    )
    """)

# cursor.execute("""INSERT INTO Funcionarios VALUES ()
#                """    
# )
