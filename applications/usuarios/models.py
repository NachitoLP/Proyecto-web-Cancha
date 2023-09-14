from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    correo = models.EmailField('Correo electrónico', max_length=254)
    telefono_celular = models.IntegerField('Telefono celular')
    contraseña = models.CharField('Contraseña', max_length=8)
    
    class Meta():
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['apellido', 'nombre']
        unique_together = ['correo']
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}"