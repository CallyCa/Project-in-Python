# Remove o arquivo com o banco de dados SQLite(caso exista)
import os
os.remove("date.db") if os.path.exists("date.db") else None
# Importando o modulo de acesso ao SQLite
import sqlite3

# Criando uma conexao com o banco de dados
conn = sqlite3.connect("date.db")
type(conn)
# Criando um cursor
c = conn.cursor()
type(c)
# Cria uma funcao para criar uma tabela, caso a tabela nao exista
# Ele cria uma nova tabela com as propriedades assim definidas.
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
               'prod_name TEXT, valor REAL)')

# Insere dados na tabela produtos
# conn = conexao; commit = salva os dados inseridos no sql; c.close = fecha a conexao com o cursor
# conn.close fecha a conexao com o sql
def data_insert():
    c.execute("INSERT INTO produtos VALUES(10, '2020-05-02 14:30:11', 'Teclado', 90)")
    conn.commit() 
   
# Chama a funcao para criar a tabela
create_table()
# Chama a funcao para inserir os dados na tabela
data_insert()

# Ira fazer uma consulta query na tabela produtos
sql_select = "select * from produtos"

# Seleciona todos os registros e recupera os registros
# Fetchall irá pegar todos os registros e salvar no objeto dados.
c.execute(sql_select)
dados = c.fetchall()

# Lista todo o conteúdo
for linha in dados:
    print("ID: %d, Data: %s, Produto: %s, Preco: %d \n" % linha)
    
# Fecha o cursor do banco de dados.
# # Fecha a conexão do banco de dados.
c.close()
conn.close()