import mysql.connector
from mysql.connector import Error


try:   
    con = mysql.connector.connect(host='localhost',database='Supercheckout', user='root', password = 'root')
    coluna = (raw_input('Digite a coluna que deseja alterar:'))
    valor_novo =(raw_input('Digite o texto ou valor que deseja alterar: '))
    valor_atual =(raw_input('Digite o nome ou valor que sera substituido:'))
    consulta_sql = "UPDADE Supercheckout.checkout_business_information SET '%s' = '%s' where '%s'  = %s"%(coluna,valor_novo,coluna,valor_atual)
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    con.commit()
    
    
except Error as e:
    print ('Erro ao acessar tabela Mysql', e)
finally:

    if con.is_connected():
        con.close()
        print ('Conexao Encerrada')

