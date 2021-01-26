import mysql.connector
from mysql.connector import Error


try:   
    con = mysql.connector.connect(host='localhost',database='Supercheckout', user='root', password = 'root')
    valor = (raw_input('Digite o ID:'))
    
    consulta_sql = "DELETE FROM Supercheckout.checkout_business_information where id = %s;"%valor
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    con.commit()
    
    
except Error as e:
    print ('Erro ao acessar tabela Mysql', e)
finally:

    if con.is_connected():
        con.close()
        print ('Conexao Encerrada')

       