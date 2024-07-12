from django.contrib import admin
from .models import Genero, Cliente, Auto

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id_genero', 'genero')
    list_display_links = ('id_genero', 'genero')
    search_fields = ('genero',)
    list_per_page = 20

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'telefono', 'email')
    list_display_links = ('rut', 'nombre')
    search_fields = ('rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'email')
    list_per_page = 20

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('Marca', 'nombre', 'color', 'cant_pasajeros', 'annio', 'tipo_vehiculo', 'combustible', 'valor')
    list_display_links = ('Marca', 'nombre')
    search_fields = ('Marca', 'nombre', 'tipo_vehiculo', 'combustible')
    list_per_page = 20
