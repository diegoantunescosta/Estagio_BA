import mysql.connector
from mysql.connector import Error


try:

        
    con = mysql.connector.connect(host='localhost',database='Supercheckout', user='root', password = 'root')
    escolher_consulta = raw_input('Digite o numero:')
    consulta_sql = ('SELECT * FROM Supercheckout.checkout_business_information where id like {}'.format(escolher_consulta))
    cursor = con.cursor ()
    cursor.execute (consulta_sql)
    linhas = cursor.fetchall ()
    print ('Numero total de registros retornandos:',cursor.rowcount)



    print('\nMostrando os dados cadastrados no DB')
    for linha in linhas:
        print('id:',linha[0])
        print('Name:',linha[1])
        print('Business Name:',linha[2] )
        print ('-'* 50)

except Error as e:
    print ('Erro ao acessar tablea Mysql', e)

finally:

    if con.is_connected():
        
        con.close()
        print ('Conexao Encerrada')