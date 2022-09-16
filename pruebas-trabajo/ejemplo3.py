n=int(input("Ingrese el numero: "))
if (n==0):
    print("ERROR")
else:
    for fila in range(n):
        for columna in range(n):
            if (fila == 0 or fila == 5) and (columna==0 or columna==5):
                print ("X",end="")
            elif (fila == 1 or fila==4)and(columna==1 or columna==4):
                print("X",end="")
            elif (fila==2 or fila==3) and (columna==2 or columna==3):
                print("X",end="")
            else:
                print("_",end="") 
    
        print()
