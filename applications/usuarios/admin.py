from django.contrib import admin
from .models import Usuarios
# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'correo',
        'telefono_celular'
    )
    list_display_links = ('correo',)
    list_editable = ('telefono_celular',)
    list_filter = ('correo',)

admin.site.register(Usuarios,UsuariosAdmin)