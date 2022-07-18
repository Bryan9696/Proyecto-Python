import usuarios.usuario as modelo
import notas.acciones  
class Acciones:
  
    def registro(self):
         print("\nOK!! Vamos a registrarte en el sistema...")
 
         nombre = input("Ingrese su nombre?: ")
         apellidos = input("Cuales son tus apellidos?: ")
         email = input("Introduce tu email: ")
         password = input("Introduce tu contraseña: ")
         
         usuario = modelo.Usuario(nombre,apellidos,email,password)
         registro = usuario.registrar() 

         if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
         else:
            print("No te has registrado correctamente")   


    def login(self):
        print("\nVale!! Identificate en el sistema...")    

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario =  modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:   
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")  
                self.proximasAcciones(login) 

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo mas tarde")    


    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles:
        -Crear notas (crear)
        -Mostrar notas (mostrar)
        -Eliminar notas (eliminar)
        -Salir (salir)
        """)

        accion = input("Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            #print("vamos a crear")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
            

        elif accion=="eliminar":
            #print("vamos a eliminar")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion=="salir":
            print(f"Ok {usuario[1]}, hasta pronto!!!")
            exit()

    