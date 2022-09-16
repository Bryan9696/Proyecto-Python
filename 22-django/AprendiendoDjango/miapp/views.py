from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from miapp.models import Article

# Create your views here.
#MVC = Modelo Vista Controlador --> Acciones (metodos) 
#MTV = Modelo Template Vista --> Acciones (metodos)

#def index(request):
#    return HttpResponse("""
#        <h1> Inicio </h1>    
#    """)


layout = """
<h1>Stio Web con Django | Victor Robles</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>

    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>

    <li>
        <a href="/paginas-prueba">Pagina de Pruebas</a>
    </li>

    <li>
        <a href="/contacto-dos">Contactos</a>
    </li>

</ul>
<hr/>        
"""

def index(request):

    """
    html=""
        <h1> Inicio </h1>
        <p> Años hasta el 2050: </p>
        <ul> 
    ""
    year = 2021
    while year <= 2050:

        if year % 2==0:
            html += f"<li>{str(year)}</li>"
        
        year += 1

    html+="</ul>"
    """

    year = 2021
    hasta = range(year,2051)

    nombre="Bryan"
    lenguajes=['JavaScript','Python','PHP','C']

    return render(request,'index.html', {
        'title':'Inicio 2',   
        'mi_variable':'Soy un dato que esta en la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'years':hasta
    })

def hola_mundo(request):
    return render(request,'hola_mundo.html')

def pagina(request,redirigir = 0):

    if redirigir ==1:
        #return redirect('/contacto/bryan/pintado')
        return redirect('contacto',nombre='Bryan',apellido='Pintado')

    return render(request,'pagina.html',{
        'texto':''
    })

def contacto(request,nombre="",apellido=""):
    html=""
    if nombre and apellido:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

def crear_articulo(request):
    articulo = Article(
        title = 'Primer Articulo',
        content = 'Contenido del articulo',
        public = True
    )

    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.title}-{articulo.content} ")

    