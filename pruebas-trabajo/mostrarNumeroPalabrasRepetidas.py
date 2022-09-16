#text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar"

def numeroPalabrasRep(text):
    texto =  text.lower()
    diccionary = {}

    for word in texto.replace(',','').split(" "):
     if word in diccionary: 
        diccionary[word] += 1
     else:
        diccionary[word] = 1 
    #print(diccionary)
    print(diccionary)


numeroPalabrasRep("Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar")