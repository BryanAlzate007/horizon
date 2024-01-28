from rest_framework import routers
from .viewsets import HorizonViewSet
from django.urls import path
from .views import UserCreate

router = routers.SimpleRouter()
router.register('horizon', HorizonViewSet)


urlpatterns = router.urls 

urlpatterns = [
    path('api/form-submit/', UserCreate.as_view()),
]
