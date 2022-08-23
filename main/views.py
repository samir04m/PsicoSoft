from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("No es posible ingresar con este usuario. Póngase en contacto con el administrador.")
    else:
        return render(request, 'login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def Inicio(request):
    return HttpResponse("Hello, world. You're at the polls index.")