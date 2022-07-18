"""
Proyecto Python  y Mysql
-Abrir asistente
-Login o registro
-Si elegimos registro, creara  un usuario en la bbdd
-Si elegimos login, identificara al usuario y nos preguntara 
-Crear nota, mostrar nota, borrarlas.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -registro
    -login
""")

hazEl = acciones.Acciones()

accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login() 


