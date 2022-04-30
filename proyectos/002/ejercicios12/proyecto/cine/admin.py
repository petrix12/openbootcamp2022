from django.contrib import admin
from . models import Pelicula, Director

# Registrar modelos en el panel de administración
admin.site.register(Pelicula)
admin.site.register(Director)
