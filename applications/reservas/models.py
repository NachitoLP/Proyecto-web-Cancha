from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Horarios(models.Model) :
    option = models.TimeField('Horario', default='')
    
    class Meta:
        ordering = ['option']
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
    
    def __str__(self):
        return str(self.option)

class Reserva(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    date = models.DateField('Fecha', default='')
    hour = models.ForeignKey(Horarios, on_delete=models.CASCADE, verbose_name='Horario', default='')
    
    class Meta:
        ordering = ['date']
        verbose_name = 'Fecha'
        verbose_name_plural = 'Fechas'
    
    def __str__(self):
        return str(self.date) + ' / ' + str(self.hour) + ' - ' + str(self.user.last_name) + ' ' + str(self.user.first_name)