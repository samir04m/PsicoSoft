from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .structures import *

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            alert = Alert("El usuario o la contraseña son incorrectos.", "danger")
            return render(request, 'login.html', {"username": username, "alert": alert})
    else:
        return render(request, 'login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def Inicio(request):
    return render(request, 'inicio.html')