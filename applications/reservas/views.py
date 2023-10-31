from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Reserva, Horarios

# Create your views here.

def reservarCancha(request) :
    from datetime import date, datetime
    import time
    
    today = datetime.now()
    print(today)
    alias = "Joaquin.Lopez.Ig"
    valorSeña = 2500
    
    if request.method == 'GET' :
        return redirect('http://127.0.0.1:8080/')
    else :
        horario = Horarios.objects.get(
            option = request.POST["horario"]
        )
        
        # Horario formateado
        newHorario = time.strptime(request.POST["horario"], '%H:%M:%S')
        
        newDate = request.POST['dia']
        
        # Fecha formateada
        date = datetime.strptime(newDate, '%Y-%m-%d')
        
        queryset = Reserva.objects.filter(
            date = date,
            hour = horario
        )
        if request.user.is_authenticated:
            if not queryset :
                # Año mayor o igual al año actual
                if date.year >= today.year :
                    # En caso de que el mes sea mayor al mes actual, cualquier día.
                    if date.month > today.month :
                        reserva = Reserva.objects.create(
                            date = date,
                            hour = horario,
                            user = request.user
                        )
                        reserva.save()
                        messages.success(request, f'¡Se ha realizado la reserva con éxito! Tenés hasta 24hs hábiles para enviar la seña, es decir, ${valorSeña}, al alias: {alias}.')
                        return redirect('http://127.0.0.1:8080/')
                    # En caso de que el mes sea el mismo que el actual, mayor o igual el día.
                    elif date.month == today.month :
                        if date.day > today.day:
                            reserva = Reserva.objects.create(
                                date = date,
                                hour = horario,
                                user = request.user
                            )
                            reserva.save()
                            messages.success(request, f'¡Se ha realizado la reserva con éxito! Tenés hasta 24hs hábiles para enviar la seña, es decir, ${valorSeña}, al alias: {alias}.')
                            return redirect('http://127.0.0.1:8080/')
                        elif date.day == today.day :
                            # Mismo día, horario mayor al horario actual
                            if newHorario.tm_hour > today.hour :
                                reserva = Reserva.objects.create(
                                    date = date,
                                    hour = horario,
                                    user = request.user
                                )
                                reserva.save()
                                messages.success(request, f'¡Se ha realizado la reserva con éxito! Tenés hasta 24hs hábiles para enviar la seña, es decir, ${valorSeña}, al alias: {alias}.')
                                return redirect('http://127.0.0.1:8080/')
                            else :
                                # Hora anterior a la hora actual
                                messages.error(request, '¡Ups! No se puede reservar el horario seleccionado ya que ya pasó. Probá nuevamente con otro horario y/o fecha.')
                                return redirect('http://127.0.0.1:8080/')
                        else :
                            # Día anterior en el mismo mes
                            messages.error(request, '¡Ups! No se puede reservar el día seleccionado ya que ya pasó. Probá nuevamente con otra fecha.')
                            return redirect('http://127.0.0.1:8080/')
                    else :
                        # Mes anterior al actual
                        messages.error(request, '¡Ups! No se puede reservar el día seleccionado ya que ya pasó. Probá nuevamente con otra fecha.')
                        return redirect('http://127.0.0.1:8080/')
                else :
                    # Año anterior al actual
                    messages.error(request, '¡Ups! No se puede reservar el día seleccionado ya que ya pasó. Probá nuevamente con otra fecha.')
                    return redirect('http://127.0.0.1:8080/')
            else:
                messages.error(request, '¡Ups! No se encuentra disponible ese horario.')
                return redirect('http://127.0.0.1:8080/')
        else: 
            messages.error(request, '¡Debés iniciar sesión para poder reservar!')
            return redirect('http://127.0.0.1:8080/')