from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Consultas
# Create your views here.

def consultas(request) :
    if request.method == 'GET' :
        return redirect('http://127.0.0.1:8080/')
    else :
        consulta = Consultas.objects.create(
            name = request.POST['name_contacto'],
            email = request.POST['correo_contacto'],
            description = request.POST['consulta_contacto']
        )
        consulta.save()
        messages.info(request, '¡Se ha enviado la consulta correctamente! Estaremos respondiéndote a la brevedad.')
        return redirect('http://127.0.0.1:8080/')