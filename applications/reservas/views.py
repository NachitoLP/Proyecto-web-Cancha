from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Reserva, Horarios

# Create your views here.

def reservarCancha(request) :
    alias = "Joaquin.Lopez.Ig"
    valorSeña = 2500
    
    if request.method == 'GET' :
        return redirect('http://127.0.0.1:8080/')
    else :
        horario = Horarios.objects.get(
            option = request.POST["horario"]
        )
        queryset = Reserva.objects.filter(
            date = request.POST['dia'],
            hour = horario
        )
        if request.user.is_authenticated:
            if not queryset :
                reserva = Reserva.objects.create(
                    date = request.POST['dia'],
                    hour = horario,
                    user = request.user
                )
                reserva.save()
                messages.success(request, f'¡Se ha realizado la reserva con éxito! Tenés hasta 24hs hábiles para enviar la seña, es decir, ${valorSeña}, al alias: {alias}.')
                return redirect('http://127.0.0.1:8080/')
            else:
                messages.error(request, '¡Ups! No se encuentra disponible ese horario.')
                return redirect('http://127.0.0.1:8080/')
        else: 
            messages.error(request, '¡Debés iniciar sesión para poder reservar!')
            return redirect('http://127.0.0.1:8080/')