import sqlite3
db = sqlite3.connect('dataBase.db')
cursor = db.cursor()

cursor.execute(""" CREATE TABLE Funcionarios(
    Codigo integer, 
    Nome text,        
    Sobrenome text,
    CPF	integer,            
    Cidade	text,        
    Funcao	text,
    Salario	REAL,
    AnoNascimento integer
    )
    """)

listaDeDados = [
    ('1','Joao','Barreto','123456789','BH',"QA","500",'1999'),
    ('2','Pedro','Costa','987654321','SP',"Dev - frontend","800",'1995'),
    ('3','Ana','Silva','654987321','SP',"Vendedor","3000",'1994'),
    ('4','Paula','Almeida','123654789','RJ',"Dev - backend","550",'1990'),
    ('5','Joana','Souza','321321321','ES',"Dev - backend","5000",'1991'),
    ('6','Luis','Pereira','654654654','ES',"PO","6000",'1994'),
    ('7','Thiago','Lima','987987987','BH',"Vendedor","7000",'1991'),
    ('8','Juan','Soarez','111111111','BH',"UX","8000",'1992'),
    ('9','Clara','Seixas','222222222','SP',"Financeiro","9000",'1993'),
    ('10','Lis','Guedes','333333333','RJ',"CTO","10000",'1995')      
    ]

cursor.executemany("""INSERT INTO Funcionarios VALUES (?,?,?,?,?,?,?,?)""", listaDeDados)

cursor.execute(""" CREATE TABLE Departamento(
    Codigo INTEGER, 
    Nome text,        
    Localizacao	text,            
    CodigoFuncionarioGerente INTEGER 
    )
    """)

#CodigoFuncionarioGerente = 1 >>> GERENTE
#CodigoFuncionarioGerente = 0 >>> FUNCIONARIO

listaDeDados = [
    ('1','TI','BH',"0"),
    ('2','TI','SP',"0"),
    ('3','Vendas','SP',"0"),
    ('4','TI','RJ',"0"),
    ('5','TI','ES',"0"),
    ('6','TI','ES',"0"),
    ('7','Vendas','BH',"0"),
    ('8','TI','BH',"0"),
    ('9','TI','SP',"0"),
    ('10','Gerente','RJ',"1")      
    ]

cursor.executemany("""INSERT INTO Departamento VALUES (?,?,?,?)""", listaDeDados)

db.commit()
#_____________________________________________________________________________________________________________________________#

    # A) Listar nome e sobrenome ordenado por sobrenome
cursor.execute("""SELECT Nome, Sobrenome FROM Funcionarios ORDER BY Sobrenome""")
print('\n    # A) Listar nome e sobrenome ordenado por sobrenome')
for i in cursor.fetchall():
    print(i)

    # B) Listar todos os campos de funcionários ordenados por cidade
print('\n    # B) Listar todos os campos de funcionários ordenados por cidade')
cursor.execute("""SELECT * FROM Funcionarios ORDER BY Cidade""")
for i in cursor.fetchall():
    print(i)

    # C) Liste os funcionários que têm salário superior a R$ 1.000,00 ordenados pelo nome completo
print('\n    # C) Liste os funcionários que têm salário superior a R$ 1.000,00 ordenados pelo nome completo')
cursor.execute("""SELECT * FROM Funcionarios WHERE Salario > 1000 ORDER BY Nome, Sobrenome""")
for i in cursor.fetchall():
    print(i)

    # D) Liste a data de nascimento e o primeiro nome dos funcionários ordenados do mais novo para o mais velho
print('\n    # D) Liste a data de nascimento e o primeiro nome dos funcionários ordenados do mais novo para o mais velho')
cursor.execute("""SELECT AnoNascimento, Nome FROM Funcionarios ORDER BY AnoNascimento DESC, Nome""")
for i in cursor.fetchall():
    print(i)
        
    # E) Liste o total da folha de pagamento
print('\n    # E) Liste o total da folha de pagamento')
cursor.execute("""SELECT SUM(Salario) FROM Funcionarios""")
for i in cursor.fetchall():
    print(i)

    # F) Liste o nome, o nome do departamento e a função de todos os funcionários
print('\n    # F) Liste o nome, o nome do departamento e a função de todos os funcionários')
cursor.execute("""SELECT Funcionarios.Nome, Departamento.Nome, Funcionarios.Funcao  
               FROM Funcionarios JOIN Departamento
               ON Funcionarios.Codigo = Departamento.Codigo
               ORDER BY Funcionarios.Nome
               """)
for i in cursor.fetchall():
    print(i)

    # G) Liste a quantidade de funcionários desta empresa
print('\n    # G) Liste a quantidade de funcionários desta empresa')
cursor.execute("""SELECT COUNT(*)
               FROM Funcionarios
               """)
for i in cursor.fetchall():
    print(i)

    
    # H) Liste o nome do departamento e do funcionário ordenados por departamento e funcionário
print('\n    # H) Liste o nome do departamento e do funcionário ordenados por departamento e funcionário')    
cursor.execute("""SELECT Departamento.Nome, Funcionarios.Nome  
               FROM Departamento JOIN Funcionarios
               ON Funcionarios.Codigo = Departamento.Codigo
               ORDER BY Departamento.Nome, Funcionarios.Nome
               """)
for i in cursor.fetchall():
    print(i)
