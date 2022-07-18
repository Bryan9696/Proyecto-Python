#importar modulo
from importlib.resources import path
from io import open
import pathlib
import shutil


#Abrir archivo
ruta=str(pathlib.Path().absolute())+"/fichero_texto.txt"
archivo = open(ruta,"a+") 

#Escribir 
archivo.write("*****Soy un texto metido desde python********\n")

#Cerrar archivo 
archivo.close()


#Abrir archivo
ruta=str(pathlib.Path().absolute())+"/fichero_texto.txt"
archivo_lectura = open(ruta,"r") 



# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    print(" "+frase.upper())

"""
# Copiar
ruta_original=str(pathlib.Path().absolute())+"/fichero_texto.txt"
ruta_nueva=str(pathlib.Path().absolute())+"/fichero_copiado.txt"
ruta_alterna = "../05-Condicion/fichero_copiado77.txt"
ruta_alterna2 =str(pathlib.Path().absolute()) + "/../05-Condicion/fichero_copiado77.txt"

shutil.copyfile(ruta_original,ruta_alterna)
"""

"""
#Mover
ruta_original=str(pathlib.Path().absolute())+"/fichero_copiado.txt"
ruta_nueva=str(pathlib.Path().absolute())+"/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original,ruta_nueva)
"""

"""
#Eliminar
import os
ruta_nueva=str(pathlib.Path().absolute())+"/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""
#comprobar si existe
import os.path
ruta_comprobar=os.path.abspath("./")+"/fichero_texto.txt"
print(ruta_comprobar)
#print(os.path.abspath("../"))
if os.path.isfile(ruta):
    print("El fichero existe")
else:
    print("El fichero no existe")    