from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50, choices=[('local', 'Local'), ('internacional', 'Internacional')])
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.descripcion
