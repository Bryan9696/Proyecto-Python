#function invertir(texto){
#    let invertido = "";
#    for (let letra of texto){
#        console.log(letra)
#    }
#}
#invertir("victorroblesweb")

def invertido(texto):
    invertido = set();
    #a=reversed(texto)
    for invertido in texto:
        invertido.add(reversed(texto))
        print(invertido)


invertido("Victor Robles")