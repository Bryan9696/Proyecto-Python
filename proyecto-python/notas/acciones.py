import notas.nota as modelo

class Acciones:

    def crear(self,usuario):
        print(f"\nOk{usuario[1]}!!Vamos a crear una nueva nota...")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.nota(usuario[0],titulo, descripcion)
        guardar = nota.guardar()    

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")    

    def  mostrar(self, usuario):
        print(f"\nVale {usuario[1]}!!Aqui tienes tus notas: ")          
        nota = modelo.nota(usuario[0])
        notas = nota.listar() 

        for nota in notas:
            print("***************************")
            print(nota[2])     
            print(nota[3])
            print("***************************")

    def borrar(self, usuario):
        print(f"\nOkey {usuario[1]}!! Vamos a borrar notas")
        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modelo.nota(usuario[0],titulo)
        eliminar = nota.eliminar(titulo) 

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se ha borrado la nota, prueba luego...")      
        
#Cambio
