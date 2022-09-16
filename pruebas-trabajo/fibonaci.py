
def fibonacci(numero):
    serie = [0,1];

    for i in range(2,numero+1):
        serie.append(serie[i-1]+serie[i-2])
    #return [serie,serie[numero]]    
    return [serie,serie[i]]    

print(f"Serie completa: {fibonacci(15)[0]}")
print(f"Serie completa: {fibonacci(15)[1]}")