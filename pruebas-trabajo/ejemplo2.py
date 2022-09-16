"""
Una empresa que realiza pruebas de seleccion de personal, necesita conocer el puntaje total obtenido por los candidatos que 
presenten las pruebas tecnicas a un determinado empleo. El puntaje total se calcula restando del puntaje obtenido por 
respuestas correctas el obtenido por respuestas incorrentas y en blanco.
Por cada respuesta correcta se obtienen 5 puntos, respuesta incorrecta -2 puntos y respuestas en blanco -1 punto. La cantidad
total de preguntas que tienen las evaluaciones son de 20.
"""
nombre = input("Ingrese su nombre: ")
rc = int(input("Ingrese la cantidad de respuestas correctas: "))
ri = int(input("Ingrese la cantidad de respuestas incorrectas: "))
blank = 20 -rc-ri
score=rc*5 - ri*2 - blank*1
print(f"El resultado obtenido por {nombre} es: {score} ")