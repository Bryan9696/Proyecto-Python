import os


#crear carpeta
if not os.path.isdir("./mi_carpeta3"):
    os.mkdir("./mi_carpeta3")
else:
    print("ya existe el directorio")    


#eliminar carpeta
#os.rmdir('./mi_carpeta3_copiada')

""" 
#copiar carpeta
import shutil
ruta_original="./mi_carpeta3"
ruta_nueva="./mi_carpeta3_copiada"
shutil.copytree(ruta_original,ruta_nueva)
"""

print("Contenido de mi carpeta:")
contenido=os.listdir("./mi_carpeta3")

for fichero in contenido:
    print("Fichero: "+fichero)