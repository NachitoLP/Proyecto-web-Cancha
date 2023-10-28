from django.db import models

# Create your models here.

class Consultas(models.Model):
    name = models.CharField('Nombre', max_length=50)
    email = models.EmailField('Email', max_length=254)
    description = models.TextField('Consulta', max_length=500)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
    
    def __str__(self):
        return self.name