
def numerosDiferentes(numeros):
    if len(numeros) == len(set(numeros)):   
         return True
    else:
        return False 


print(numerosDiferentes([2,4,5,7,9]))
print(numerosDiferentes([2,4,5,5,7,9]))

#Escriba un programa de Python para crear todas las
#cadenas posibles usando 'a', 'e', ​​'i', 'o', 'u'. Usa los caracteres exactamente una vez.
import random
char_list=['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))


