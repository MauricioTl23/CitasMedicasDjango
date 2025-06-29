# HttpRequest: Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader


#New view (pasando como parametro un request)

def obtenermomentoactual(request):
    respuesta = "<h1>Momento Actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return  HttpResponse(respuesta)

def firstSquad(request):
    nombre = "Mauricio Dimas Teran Limari"
    dep = {"Oruro","La Paz","Potosi","Cochabamba","Tarija","Sucre","Pando","Beni","Santa Cruz"}
    fechaActual = datetime.datetime.now()
    plantillaexterna = open("/Users/mauricioteranlimari/Documents/PythonProject/Django/PrimerProyecto/PrimerProyecto/Plantillas/FirstSquad.html")
    template = Template(plantillaexterna.read())
    plantillaexterna.close()
    contexto = Context({"Nombre":nombre,"FechaActual":fechaActual,"departamentos":dep})
    documento = template.render(contexto)
    return HttpResponse(documento)

def loaderTemplate(request):
    nombre = "Mauricio Dimas Teran Limari"
    dep = {"Oruro", "La Paz", "Potosi", "Cochabamba", "Tarija", "Sucre", "Pando", "Beni", "Santa Cruz","El Alto"}
    fechaActual = datetime.datetime.now()
    #abrir la plantilla, especifica en una variable
    plantillaExterna = loader.get_template('FirstSquad.html')
    documento = plantillaExterna.render({"Nombre":nombre,"FechaActual":fechaActual,"departamentos":sorted(dep)})
    return HttpResponse(documento)

#Metodo simple y correcto de llamar a las plantillas,
#los demas metodos son muy ambiguos
def plantillashortcut(request):
    nombre = "Mauricio Dimas Teran Limari 7455337-OR"
    dep = {"Oruro", "La Paz", "Potosi", "Cochabamba", "Tarija", "Sucre", "Pando", "Beni", "Santa Cruz", "El Alto"}
    fechaActual = datetime.datetime.now()

    return render(request,'FirstSquad.html',{"Nombre":nombre,"FechaActual":fechaActual,"departamentos":sorted(dep)},)

def MenuTemplate(request):
    return render(request,"MenuTemplate.html",{})

def ContactTemplate(request):
    return render(request,"ContactTemplate.html",{})