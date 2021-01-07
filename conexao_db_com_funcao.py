#Remove o arquivo com o banco de dados SQlite (caso exista)
import os
os.remove('dsa.db') if os.path.exists('dsa.db') else None

import sqlite3


# criando uma conexão
conn = sqlite3.connect('dsa.db')

#Criando um cursor
c= conn.cursor()

#função para criar uma tabela
def create_table():
    c.execute ('CREATE TABLE produtos( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,'\
     'prod_name TEXT, valor REAL)')


# Função para inserir uma linha

def data_insert ():
    c.execute ("INSERT INTO produtos VALUES(10,'2018-05-02 14:32:11','Teclado',90)")
    conn.commit()
    c.close()
    conn.close()

    #criar tabela
create_table()
    #inserir dados
data_insert()


