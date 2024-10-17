from django.db import models

# Create your models here.
class Producto(models.Model):
    CATEGORIAS = [
        ('TV', 'Televisor'),
        ('LP', 'Laptop'),
        ('ES', 'Equipo de Sonido'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=2, choices=CATEGORIAS)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombrep