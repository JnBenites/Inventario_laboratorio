from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Laboratorio, Estado, TipoMantenimiento, Equipo, Mantenimiento
from .models import Case, Monitor,Teclado, Raton,Parlante, Impresora, Proyector, Ups
# Register your models here.

admin.site.register(Laboratorio)
admin.site.register(Estado)
admin.site.register(TipoMantenimiento)
admin.site.register(Equipo)
admin.site.register(Mantenimiento)

# computador
admin.site.register(Case)
admin.site.register(Monitor)
admin.site.register(Teclado)
admin.site.register(Raton)
admin.site.register(Parlante)
admin.site.register(Impresora)
admin.site.register(Proyector)
admin.site.register(Ups)


admin.site.site_header = 'Inventario 😆'
admin.site.site_title = 'Inventario 😂'