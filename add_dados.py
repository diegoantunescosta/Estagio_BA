import mysql.connector
from mysql.connector import Error


try:   
    con = mysql.connector.connect(host='localhost',database='Supercheckout', user='root', password = 'root')
    indentificacao = (raw_input('Digite o ID:'))
    nome_pessoal = str (raw_input('Digite seu nome:'))
    nome_empresa = str (raw_input('Digite o Nome da empresa:'))

    consulta_sql = "insert into Supercheckout.checkout_business_information (id, name, business_name) values ('%s','%s','%s')"%(indentificacao,nome_pessoal,nome_empresa)
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    con.commit()
    
except Error as e:
    print ('Erro ao acessar tabela Mysql', e)
finally:

    if con.is_connected():
        con.close()
        print ('Conexao Encerrada')
