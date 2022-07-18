"""
#Condicion If

Si se_cumple_esta_condicion:
   Ejecuta grupo de instrucciones
SI NO:
    Se ejecuta otro grupo de condiciones

if condicion:
    instrucciones
else:
    otras instrucciones    

#Operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que 

#Operadoeres logicos 
and significa y
or  significa O
!   significa negacion
not significa no


"""

#IFs anidados
nombre = "Bryan Pintado"
ciudad = "Buenos Aires"
continente = "America"
edad = 15
mayoriaEdad = 18

if edad >= mayoriaEdad:
    print(f"{nombre} es mayor de edad !!")

    if continente !=  "Europa":
        print(f"El usuario no es Europeo")
    else:
        print(f"Es europeo y de {ciudad}")    
else:
    print(f"{nombre} no es mayor de edad")