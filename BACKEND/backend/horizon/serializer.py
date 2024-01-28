from rest_framework import serializers
from .models import Horizon, User

class HorizonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horizon
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombre', 'tipo_documento', 'numero_documento', 'edad', 'fecha_nacimiento', 'lugar_nacimiento', 'email', 'password']
        # No incluir confirmPassword
