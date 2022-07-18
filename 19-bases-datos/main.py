import mysql.connector
import sqlite3
#Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"

)

#¿La conexion ha sido exitosa?
#print(database)

cursor = database.cursor(buffered=True)

"""
#Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
#Consulta tablas
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")    


"""
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
"""

#cursor.execute("INSERT INTO vehiculos values(null,'Chevrolet','gls 2013',10300)")
"""
coches=[
    ('Susuki','gran vitara',20000),
    ('toyota','yaris',9600),
    ('hyundai','2015',25000),
    ('chevrolet','sail',10000)
]
cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)",coches)
database.commit()
"""
cursor.execute("SELECT * FROM vehiculos WHERE precio < 20000")
result = cursor.fetchall()

print("------TODOS MIS COCHES-----")
for coche in result:
    print(coche[1],coche[3])

#Listar
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)    

#Borrar
cursor.execute("DELETE FROM vehiculos WHERE marca='toyota' ")
database.commit() 

print(cursor.rowcount,"borrados!!")

#Actualizar
cursor.execute("UPDATE  vehiculos SET modelo='GLS' WHERE marca='susuki' ")
database.commit()
print(cursor.rowcount,"Actualizados!!")
