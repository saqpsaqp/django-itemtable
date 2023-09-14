from django.db import models

class Item(models.Model):
    class Estado(models.TextChoices):
        ACTIVADO = 'Activado', 'Activado'
        DESACTIVADO = 'Desactivado', 'Desactivado'
        ELIMINADO = 'Eliminado', 'Eliminado'

    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.ACTIVADO)

    def __str__(self):
        return self.nombre
