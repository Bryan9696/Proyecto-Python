from re import I


numbers = [12,56,89,78,62,23,121,59]



print("**************RECORRER Y MOSTRAR*************")
def mostrarLista (lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemeto: "+str(elemento)
        resultado +=  "\n"

    return resultado    
"""
for n in numbers:
    print(n)
"""

print(mostrarLista(numbers))

print("**************ORDENAR  Y MOSTRAR*************")
numbers.sort()
print(mostrarLista(numbers))

print("**************MOSTRAR LONGITUD*************")
print(len(numbers))

print("**************BUSCAR NUMERO*************")
search=int(input("Ingrese el numero a buscar: "))
comprobe = isinstance(search,int)
while not comprobe or search <= 0:
    search=int(input("Ingrese el numero a buscar: "))
else:
    print(f"Has introducido {search}")

print(f"#### Buscar en la lista el numero {search} ####")
search2 = numbers.index(search)
print(f"El numero buscado existe en la lista, es el indice: {search2}")
