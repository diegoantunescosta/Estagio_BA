import mysql.connector
con = mysql.connector.connect(host='sql5.freesqldatabase.com',database='sql5389583',user='sql5389583',password='FPexFIZbKM')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versao ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

escolhe_tabela = input('Digite o nome da tabela: ')
escolhe_coluna = input ('Digite o nome da coluna: ')
escolhe_consulta = input('Digite o Valor: ')
consulta_sql = "SELECT * FROM sql5389583.{} where {} like '%{}%'".format(escolhe_tabela,escolhe_coluna,escolhe_consulta)
print(consulta_sql)
cursor = con.cursor ()
cursor.execute (consulta_sql)
linhas = cursor.fetchall ()
print ('Numero total de registros retornandos:',cursor.rowcount)

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexao ao MySQL foi encerrada")
