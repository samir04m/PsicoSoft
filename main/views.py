from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .structures import *
from .models import *

def Index(request):
    return render(request, 'index.html')

def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/pacientes')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/pacientes')
        else:
            alert = Alert("El usuario o la contraseña son incorrectos.", "danger")
            return render(request, 'login.html', {"username": username, "alert": alert})
    else:
        return render(request, 'login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required(login_url='/login/')
def PacienteList(request):
    return render(request, 'paciente/list.html')

@login_required(login_url='/login/')
def PacienteSave(request):
    if request.method == 'POST':
        try:
            paciente = Paciente(
                usuario = request.user,
                nombres = request.POST.get('nombres'),
                apellidos = request.POST.get('apellidos'),
                tipoDocumento = request.POST.get('tipoDocumento'),
                numeroDocumento = request.POST.get('numeroDocumento'),
                fecha = datetime.now()
            )
            paciente.save()
            # messages.success(request, 'Correcto', extra_tags='success')
            return redirect('main:PacienteCreate', paciente.id)
        except Exception as e:
            log = ExceptionLog(
                usuario = request.user,
                descripcion = "No se pudo crear Paciente. Metodo PacienteSave",
                excepcion = e,
                fecha = datetime.now()
            )
            log.save()
            messages.error(request, 'No fue posible crear el Paciente. Intente de nuevo.', extra_tags='danger')
            return redirect('main:PacienteList')
    else:
        return HttpResponseRedirect('/pacientes')

@login_required(login_url='/login/')
def PacienteCreate(request, id):
    return HttpResponse("hola")