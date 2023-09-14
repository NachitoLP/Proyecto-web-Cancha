from django.db import models
from ..usuarios.models import Usuarios

# Create your models here.

class Reservas(models.Model) :
    fecha_reserva = models.DateField('Fecha de reserva', auto_now=False, auto_now_add=False)
    hora_reserva = models.TimeField('Hora de reserva', auto_now=False, auto_now_add=False)
    usuario = models.ManyToManyField(Usuarios)
    
    class Meta():
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
    
    def __str__(self):
        return f"Reserva: {self.fecha_reserva} {self.hora_reserva} a nombre de {self.usuario}"