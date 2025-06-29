from django.contrib import admin
from django.urls import path

from PrimerProyecto.views import MenuTemplate,ContactTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MenuPrincipal/',MenuTemplate),
    path('Contactos/',ContactTemplate),
]
