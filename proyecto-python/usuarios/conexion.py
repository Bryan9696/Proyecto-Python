import mysql.connector


def conectar():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "master_python",
        port = 3306
    ) 

    #print(database)
    #buffered = True nos sirve para poder hacer multiples consultas con el mismo cursor
    cursor = database.cursor(buffered=True)
    
    return [database,cursor]

