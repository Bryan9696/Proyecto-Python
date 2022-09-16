from pytz import NonExistentTimeError


myArray = [13,2,4,35,11]

#menor=min(myArray)
# print(menor)

menor = None

for numero in myArray:
    if menor == None:
        menor=numero
    
    elif numero<menor:
        menor=numero
print(f"el numero menor es:{menor}")    
