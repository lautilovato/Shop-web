from django.db import models


class Zapatilla(models.Model):
    imagen = models.ImageField(upload_to= "imagenes") 
    modelo = models.CharField(max_length= 100)
    marca = models.CharField(max_length= 100)
    def __str__(self):
        return f"{self.modelo}"