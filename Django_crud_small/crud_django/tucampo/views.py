
from cgitb import html
from django.http import HttpResponse
from django.template import Template, context
from datetime import  datetime

##############
"""class persona(object):
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
def saludo(request): #primera vista
    p1=persona('jonatan',28)
    fecha=datetime.now()
    
    doc_externo=open("D:/Django/crud_django/tucampo/template/pagina.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre':p1.nombre,'edad':p1.edad,'fecha':fecha})
    texto=plt.render(ctx)
    return HttpResponse(texto)



######
class alumno(object):
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def mostrar_nota(self):
        if self.nota >3:
            resultado="aprobo"
        else:
            resultado="no aprobo"

            return resultado

def nota1(request):

        a1=alumno()
        a1.inicializar('andres',4)
        resultado=a1.mostrar_nota()
 
    
    doc_externo=open("D:/Django/crud_django/tucampo/template/pagina.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre':a1.nonbre,'resultado':resultado,'fecha':fecha})
    texto=plt.render(ctx)
    return HttpResponse(texto)
"""

#pagina principal con templete context pero con variables con contexto
def home1(request,altura,base):

    nombre="jonatan"
    edad=28
    area=(altura*base)/2
    if area>100:
        val="el area es grande"

    else:
        val="el area es pequeña"


    doc_externo=open("D:/Django/crud_django/tucampo/template/home.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=context({'nombre':nombre, 'edad':edad, 'val':val})
    texto=plt.render(ctx)
    return HttpResponse(texto)


##############
#def calculo_edad (request,ano):
 #   edad_actual=30
  #  periodo=ano-2020
   # edad_futura=edad_actual+periodo
    #text="""
    #<html>
    #<body>
    #<p>para el año %s usted va terner %s años</p>
    #</body>
    #</html>
    #"""%(ano,edad_futura)
    #return HttpResponse(text)


def home(request):
    doc_externo=open("D:/Django/crud_django/tucampo/template/home.html")
    plt=Template(doc_externo.read())
    doc_externo.close
    ctx=context()
    texto=plt.render(ctx)
    return HttpResponse(texto)

def pagina(request):
    doc_externo=open("D:/Django/crud_django/tucampo/template/pagina.html")
    plt=Template(doc_externo.read())
    doc_externo.close
    ctx=context()
    texto=plt.render(ctx)
    return HttpResponse(texto)

