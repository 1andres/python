from django.contrib import admin
from celulares.apps.ventas.models import Marca, Conectividad, Color, Celular

admin.site.register(Marca)
admin.site.register(Conectividad)
admin.site.register(Color)
admin.site.register(Celular)
