from django.db import models



class User(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    tipo_documento = models.CharField(max_length=100, null=False)
    numero_documento = models.BigIntegerField(null=False)
    correo = models.CharField(max_length=150, null=False)
    telefono = models.BigIntegerField(null=False)
    millas = models.IntegerField(null=True, blank=True)  # Opcional
    contraseña = models.CharField(max_length=255, null=False)

    def _str_(self):
        return self.nombre
    
    
class City(models.Model):
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.city
    
class Trajectory(models.Model):
    ciudad_origen = models.ForeignKey(City, on_delete=models.CASCADE, related_name='ciudad_origen_trajectories')
    ciudad_destino = models.ForeignKey(City, on_delete=models.CASCADE, related_name='ciudad_destino_trajectories')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    distancia = models.DecimalField(max_digits=64, decimal_places=2) 

    def __str__(self):
        return f"{self.ciudad_origen} to {self.ciudad_destino} - {self.precio}"

