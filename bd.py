#Remove o arquivo com o banco de dados SQLite(caso exista)
import os
os.remove("escola.db") if os.path.exists("escola.db") else None
#Importando o modulo de acesso ao SQLite
import sqlite3

# Cria uma conexao com o banco de dados
# Se o banco de dados nao existir, ele é criado neste momento.
con = sqlite3.connect("escola.db")
# Type ira verificar o tipo do objeto
type(con) 
# Criando um cursor
# Um cursor permite percorrer todos os registro em um conjunto de dados
cur = con.cursor()
type(cur)

# Cria uma instruçao SQL
sql_create = 'create table cursos '\
    '(id integer primary key, '\
     'titulo varchar(100), ' \
     'categoria varchar(140))'

# Executa a instruçao SQL no cursor
cur.execute(sql_create)

sql_insert = "insert into cursos values (?,?,?)"

recset = [(1000, "Ciencia de Dados", "Data science"),
          (1001, "Big Data Fundamentos", "Big Data"),
          (1002, "Python Fundamentos", "Analise de dados")]

for rec in recset:
    cur.execute(sql_insert, rec)

con.commit()

sql_select = "select * from cursos"

cur.execute(sql_select)
dados = cur.fetchall()

for linha in dados:
    print("Curso Id: %d, Titulo: %s, Categoria: %s \n" % linha)

con.close()
        
