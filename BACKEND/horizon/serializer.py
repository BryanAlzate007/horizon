from rest_framework import serializers
from .models import User, City, Trajectory

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombre', 'tipo_documento', 'numero_documento','correo', 'contraseña']
        # No incluir confirmPassword

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city']

class TrajectorySerializer(serializers.ModelSerializer):
    ciudad_origen = CitySerializer(read_only=True)
    ciudad_destino = CitySerializer(read_only=True)

    class Meta:
        model = Trajectory
        fields = ['ciudad_origen', 'ciudad_destino', 'precio', 'distancia']