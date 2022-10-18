from django.http import HttpResponse
from django.template import Template, Context
#from django.template import loader
from django.template.loader import get_template
from cgitb import html
from django.shortcuts import render
import datetime

#plantilla 
def pagina (request):
    plantillaExterna = open("D:/curse_django/entorno/curso/templates/home.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

#plantillas con parametros coore, nombre, fecha 
def plantillasParametros (request):
    nombre = "jonatan de jesus"
    correo = "krakenjj@hotmail.com"
    fechaActual = datetime.datetime.now()
    plantillaExterna = open("D:/curse_django/entorno/curso/templates/paginaParametros.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({"nombre": nombre, "fechaActual": fechaActual, "correo": correo})
    documento = template.render(contexto)
    return HttpResponse(documento)

#comentarios
def comentarios (request):
    """este 
    es 
    un 
    comentarios
    multilenia
    """
    nombre = "jonatan de jesus"
    correo = "krakenjj@hotmail.com"
    fechaActual = datetime.datetime.now()
    plantillaExterna = open("D:/curse_django/entorno/curso/templates/commets.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({"nombre": nombre, "fechaActual": fechaActual, "correo": correo})
    documento = template.render(contexto)
    return HttpResponse(documento)

#plantillas con un pequeño style
def plantillasParametrosColor (request):
    nombre = "jonatan de jesus"
    correo = "krakenjj@hotmail.com"
    fechaActual = datetime.datetime.now()
    lenguajes = ["python", "rubi", "javaScript", "java", "c#",
    "klotin"]
    plantillaExterna = open("D:/curse_django/entorno/curso/templates/plantillaColor.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({"nombre": nombre, "fechaActual": fechaActual, "correo": correo, "lenguajes": lenguajes})
    documento = template.render(contexto)
    return HttpResponse(documento)

#listas con formato de fecha actual
def listas (request):
    lenguajes = ["python", "rubi", "javaScript", "java", "c#",
    "klotin"]
    plantillaExterna = open("D:/curse_django/entorno/curso/templates/listas.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({ "lenguajes": lenguajes})
    documento = template.render(contexto)
    return HttpResponse(documento)

#plantilla    
    plantillaExterna = open("D:/curse_django/entorno/curso/templates/listas.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({"lenguajes": lenguajes })
    documento = template.render(contexto)
    return HttpResponse(documento)

#hora
def hora(request):
   
    plantillaExterna = open("D:/curse_django/entorno/curso/templates/hora.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

#edad
def categoriaEdad(request, edad):
    if edad>=18:
        if edad>=60:
            categoria = "tercera edad"
        else :
            categoria="adultez"
    else :
        if edad<10:
            categoria = "infancia"
        else :
            categoria ="adolescencia"
    resultado  = "<h1>categoria de las edad : %s</h1>"  %categoria
    return HttpResponse(resultado) 

#hora
def obtenerMomentoActual(request):
    repuesta= "<h1>momento actual: {0}</h1>".format(datetime.datetime.now())
    return HttpResponse(repuesta) 

#contenido html sin plantilla
def contenidohtml(request, nombre, edad):  

    contenido = """
    <html>
    <body>
    <p>nombre: %s  / edad:  %s</p>
    </body>
    </html>
    """   % (nombre, edad)  
    return HttpResponse(contenido) 

#cargadores
def plantillaCargador(request):
    nombre = "jonatan de jesus"
    correo = "krakenjj@hotmail.com"
    fechaActual = datetime.datetime.now()
    lenguajes = ["python", "rubi", "javaScript", "java", "c#",
    "klotin", "php"]  
    plantillaExterna = get_template('paginaParametros.html')
    documento =  plantillaExterna.render({"nombre": nombre, "fechaActual": fechaActual, "correo": correo, "lenguajes": lenguajes})
    return HttpResponse(documento) 

#plantillaShortcut
def plantillaShortcut(request):
    nombre = "jonatan de jesus"
    correo = "krakenjj@hotmail.com"
    fechaActual = datetime.datetime.now()
    lenguajes = ["python", "rubi", "javaScript", "java", "c#",
    "klotin", "php", "C++"]
    return render (request, 'paginaParametros.html', {"nombre": nombre, "fechaActual": fechaActual, "correo": correo, "lenguajes": lenguajes} )

#planttillas incrustadas
def plantillaHija1(request):
    return render (request, "plantillaHija_1.html",{})
    
def plantillaHija2(request):
    return render (request, "plantillaHija_2.html",{})


#barra de navegacion
#def barraNavegacion (request):