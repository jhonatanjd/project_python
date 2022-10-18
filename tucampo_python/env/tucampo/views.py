from django.http import HttpResponse
from django.template import Template, Context
from cgitb import html

def pagina (request):
    plantillaExterna = open("D:/tucampo_python/env/tucampo/templates/home.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)