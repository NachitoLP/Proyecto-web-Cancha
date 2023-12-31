from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.mail import send_mail
import json

from ..reservas.models import Horarios
# Create your views here.

with open("secrets.json") as f:
    secrets = json.load(f)

def sessionLogIn(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    elif request.method == "POST":
        if not request.POST['username'] and not request.POST['password'] :
            return render(request, 'login/login.html',{
                    "error": 'No se han completado todos los datos.'
                })
        else :
            user = authenticate(request, username = request.POST['username'] , password = request.POST['password'])
            if user is None :
                return render(request, 'login/login.html',{
                    "error": 'Los datos ingresados son incorrectos.'
                })
            else:
                login(request, user)
                return redirect('http://127.0.0.1:8080/')

def sessionRegister(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    elif request.method == "POST":
        if not request.POST['email'] and not request.POST['password'] and not request.POST['username']:
            return render(request, 'login/login.html',{
                    "error": 'No se han completado todos los datos.'
                })
        else :
            try:
                
                subject = f"¡Bienvenido, {request.POST['first_name']}!"
                emailText = f'Tu usuario se ha registrado con éxito. ¡A partir de ahora podés reservar nuestro espacio cuando gustes!'
                email_from = secrets['EMAIL_HOST']
                
                user = User.objects.create_user(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password']
                    )
                user.save()
                
                email_receiver = user.email
                send_mail(subject, emailText, email_from, [email_receiver])
                
                login(request, user)
                return redirect('http://127.0.0.1:8080/')
            except IntegrityError:
                return render(request, 'login/login.html',{
                    "error": '¡El usuario ingresado ya existe!'
                })

def sessionLogOut(request) :
    logout(request)
    return redirect('http://127.0.0.1:8080/')


class IndexView (ListView) :
    model = Horarios
    template_name = 'home/index.html'
