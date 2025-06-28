from django.contrib import admin
from django.urls import path

from PrimerProyecto.views import welcome,welcome1,agecategory,obtenermomentoactual,firstSquad,loaderTemplate,plantillashortcut,MenuTemplate,ContactTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',welcome),
    path('CSS/',welcome1),
    path('AgeCategory/<int:age>',agecategory),
    path('Fecha/',obtenermomentoactual),
    path('Plantilla/',firstSquad),
    path('PlantillaLoader/',loaderTemplate),
    path('PlantillaLoaderSC/',plantillashortcut),
    path('MenuPrincipal/',MenuTemplate),
    path('Contactos/',ContactTemplate),
]
