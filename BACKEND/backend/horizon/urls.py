from rest_framework import routers
from .viewsets import HorizonViewSet
from django.urls import path
from .views import UserCreate

router = routers.SimpleRouter()
router.register('horizon', HorizonViewSet)


urlpatterns = router.urls 

urlpatterns = [
    path('createuser/', UserCreate.as_view()),
     
    #path('registrarCurso/', registrar_curso),
    #path('eliminacionCurso/<int:id>', eliminar_curso),
    #path('edicionCurso/<int:id>', edicion_curso),
    #path('editarCurso/', editar_curso),
    #path('contacto/', contacto),
]