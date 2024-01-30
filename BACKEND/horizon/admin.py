from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, City, Trajectory

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_documento', 'numero_documento', 'correo', 'telefono', 'millas')
    search_fields = ('nombre', 'correo', 'numero_documento')  # Campos por los cuales se puede buscar
    list_filter = ('tipo_documento',)  # Filtros en la interfaz de administración

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city',)

@admin.register(Trajectory)
class TrajectoryAdmin(admin.ModelAdmin):
    list_display = ('ciudad_origen', 'ciudad_destino', 'precio', 'distancia')
    search_fields = ('ciudad_origen__city', 'ciudad_destino__city')  # Búsqueda por nombre de ciudad
    list_filter = ('ciudad_origen__city', 'ciudad_destino__city')  # Filtros por ciudad de origen y destino
