from django.db import models

# Create your models here.

class persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    dui = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)



    def str(self) -> str:
        return super().str() + self
