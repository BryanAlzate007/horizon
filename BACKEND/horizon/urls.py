from django.urls import path
from .views import UserCreate

urlpatterns = [
    path('createuser/', UserCreate.as_view(), name='createuser'),


     
    #path('registrarCurso/', registrar_curso),
    #path('eliminacionCurso/<int:id>', eliminar_curso),
    #path('edicionCurso/<int:id>', edicion_curso),
    #path('editarCurso/', editar_curso),
    #path('contacto/', contacto),
]