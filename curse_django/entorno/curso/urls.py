"""curso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from curso import views
from curso.views import pagina, plantillaHija2,plantillasParametros,hora,categoriaEdad,obtenerMomentoActual,contenidohtml,listas
from curso.views import plantillasParametrosColor,comentarios,plantillaCargador,plantillaShortcut,plantillaHija1
from curso.views import plantillaHija2,poo,poo1,baseHija1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina/', pagina),
    path('parametros/', plantillasParametros), 
    path('hora/', hora),
    path('categoriaEdad/<int:edad>', categoriaEdad), 
    path('obtenerMomentoActual/', obtenerMomentoActual),
    path('contenido/<nombre>/<int:edad>', contenidohtml),
    path('lista/', listas),
    path('plantillaColor/', plantillasParametrosColor),
    path('comentario/', comentarios), 
    path('cargador/', plantillaCargador),  
    path('shortcut/', plantillaShortcut),
    path('hija/', plantillaHija1),
    path('hija1/', plantillaHija2),
    path('poo/',poo ),
    path('po/',poo1 ),
    path('bh/',baseHija1),




]
