from django.contrib import admin
from .models import Encargado, Laboratorio, Estado, TipoMantenimiento, Equipo, Mantenimiento

# Register your models here.

admin.site.register(Encargado)
admin.site.register(Laboratorio)
admin.site.register(Estado)
admin.site.register(TipoMantenimiento)
admin.site.register(Equipo)
admin.site.register(Mantenimiento)