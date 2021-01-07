import sqlite3
import random
import time
import datetime
import os
#Remove o arquivo com o banco de dados SQlite (caso exista)



#Criando uma conexão

conn =sqlite3.connect ('dsa.db')

#criando um cursor

c= conn.cursor()

#função para criar uma tabela
# def create_table():
#     c.execute ('CREATE TABLE produtos( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,'\
#      'prod_name TEXT, valor REAL)')


# Função para inserir uma linha

# def data_insert ():
#     c.execute ("INSERT INTO produtos VALUES(10,'2018-05-02 14:32:11','Teclado',90)")
#     conn.commit()
   
    

#Usando variaveis para inserir dados

def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'monitor'
    new_valor = random.randrange(50,100)
    c.execute("INSERT INTO produtos (date, prod_name,valor)VALUES (?,?,?)",
             (new_date,new_prod_name,new_valor))
    conn.commit()    

# Leitura de dados
def leitura_todos_dados():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha)

# Leitura de registros
def leitura_registros():
    c.execute("SELECT * FROM PRODUTOS WHERE valor > 60.0")
    for linha in c.fetchall():
        print(linha)

# Leitura de colunas específicos
def leitura_colunas():
    c.execute ("SELECT * FROM  PRODUTOS")
    for linha in c.fetchall():
        print (linha[3])


# create_table()
# data_insert ()
data_insert_var()
leitura_todos_dados()
leitura_registros()
leitura_colunas()
c.close()
conn.close()