#Importar modulo
import sqlite3 

#Conexion base de datos
conexion = sqlite3.connect('./19-bases-datos/pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("""
CREATE TABLE  IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
);
""")

#Guardar cambios
conexion.commit()

"""
#Insertar datos
cursor.execute("INSERT INTO productos VALUES (null,'Segundo producto','Descripcion de mi producto',550)")
conexion.commit()
"""

#Borrar registros de una tabla 
cursor.execute("DELETE FROM productos")
conexion.commit()

#Insertar muchos registros de golpe
productos = [
    ("Ordenador Portatil","Buen PC",700),
    ("Movil","Buen Telefono",140),
    ("Placa Base","Buena Placa",80),
    ("Tablet 15","Buena Tablet",300),
]
cursor.executemany("INSERT INTO productos values (null,?,?,?)",productos)
conexion.commit()

#Update
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

#Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >=300;")
#print(cursor)  Ve si esta el objeto base de datos

# imprime los datos que tengo dentro de mi base de datos
productos = cursor.fetchall()
for producto in productos:
    print("Titulo: ", producto[1])
    print("Descripcion: ",producto[2])
    print("Precio: ", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")

#Saca el primero registro de la consulta
producto = cursor.fetchone()
print(producto)

#Cerrar conexion
conexion.close()
