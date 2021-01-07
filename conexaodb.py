import os
import sqlite3
os.remove ('teste.db') if os.path.exists('teste.db') else None
con = sqlite3.connect('teste.db')
print (type(con))

cur = con.cursor()

sql_create = 'create table cursos' \
'(id integer primary key,'\
'titulo varchar(100),'\
'categoria varchar (140))'

cur.execute(sql_create)

sql_insert = 'insert into cursos values (?,?,?)'

recset =[(1000, 'Ciencia de dados ', 'Data Science'),
        (1001, 'Big data Fundamento ', 'Big Data'),
        (1002, 'Python fundamento ', 'Analise de dados')]

for rec in recset:
    cur.execute(sql_insert,rec)

con.commit()

sql_select = 'select * from cursos'

cur.execute(sql_select)
dados = cur.fetchall ()

for linha in dados:
    print ('Curso Id : %d, Titulo : %s, Categoria: %s \n'%linha)

    con.close()