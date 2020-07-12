# Necessario importar o MongoClient para conectar com a aplicação do Mongodb
from pymongo import MongoClient
# Aqui importa o horário local do computador
import datetime
# A variável conn irá armazenar conexão local com o MongoClient e a porta 27017
# É sempre necessário estar com o Mongod aberto no cmd para funcionar
conn = MongoClient("localhost", 27017)

# Aqui criar um banco de dados chamado cadastrodb
db = conn.cadastrodb

# Em MongoDB collection é parecido com um conceito de Tabelas em BD relacional
collection = db.cadastrodb

# Aqui irá informar os dados que serão inseridos na collection

post = {"codigo": "ID- 9999",
        "prod_name": "Geladeira",
        "marcas": ["brastemp","janaina","consul"], 
        "data_cadastro": datetime.datetime.utcnow()}

# Irá coletar os dados armazenados na variável post e inserir em um db
collection = db.post
# Irá inserir os dados armazenados em post na collection
post_id = collection.insert_one(post)
# Insere um ID ou uma numeração para esta collection
post_id.inserted_id

# Percorre a collection, com a funçao find() ele retorna um cursor
for post in collection.find():
    print(post)

# Verifica o nome do banco de dados
db.name
# Lista as collections disponíveis
db.list_collection_names()
