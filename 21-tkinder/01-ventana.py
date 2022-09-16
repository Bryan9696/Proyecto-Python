#tkinder
#Modulo para crear interfaces graficas de usuario

from tkinter import *   

#Crear la ventana raiz
ventana=Tk()


#Cambio en el tamaño de la ventana
ventana.geometry("750x450")

#Titulo de la ventana
ventana.title("Interfaz grafica con Python")

#Icono de la ventana 
ventana.iconbitmap("./21-tkinder/imagenes/cafe.ico")

#Bloquear el tamaño de la ventana
ventana.resizable(0,0)

#Arancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
