from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import datetime
from .structures import *
from .selectBuilder import *
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

def saveLog(usuario, descripcion, excepcion):
    try:
        log = ExceptionLog(
            usuario = usuario,
            descripcion = descripcion,
            excepcion = excepcion,
            fecha = datetime.now()
        )
        log.save()
    except Exception as e:
        print("  ===>  Error: No se puede guardar log. Exception: "+str(e))

@login_required(login_url='/login/')
def PacienteList(request):
    pacientes = Paciente.objects.filter(usuario = request.user)
    context = {
        "pacientes": pacientes,
        "selectTipoDocumento": GetSelectTipoDocumento()
    }
    return render(request, 'paciente/list.html', context)

@login_required(login_url='/login/')
def PacienteCreate(request):
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
            return redirect('main:PacienteUpdate', paciente.id)
        except Exception as e:
            saveLog(request.user, "No se pudo crear Paciente. Metodo PacienteCreate", e)
            messages.error(request, 'No fue posible crear el Paciente. Intente de nuevo.', extra_tags='danger')
            return redirect('main:PacienteList')
    else:
        return HttpResponseRedirect('/pacientes')

@login_required(login_url='/login/')
def PacienteUpdate(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    selectData = GetSelectData(paciente)
    context = {
        "paciente": paciente,
        "selectData": selectData
    }
    if request.method == 'POST':
        try:
            paciente.nombres = request.POST.get('nombres')
            paciente.apellidos = request.POST.get('apellidos')
            paciente.tipoDocumento = request.POST.get('tipoDocumento')
            paciente.numeroDocumento = request.POST.get('numeroDocumento')
            # paciente.fechaNacimiento = request.POST.get('fechaNacimiento')
            paciente.sexo = request.POST.get('sexo')
            paciente.estadoCivil = request.POST.get('estadoCivil')
            paciente.direccion = request.POST.get('direccion')
            paciente.celular = request.POST.get('celular')
            paciente.telefono = request.POST.get('telefono')
            paciente.nivelEducativo = request.POST.get('nivelEducativo')
            paciente.ocupacion = request.POST.get('ocupacion')
            paciente.motivoConsulta = request.POST.get('motivoConsulta')
            paciente.antecedentesPersonales = request.POST.get('antecedentesPersonales')
            paciente.antecedentesPersonales = request.POST.get('antecedentesPersonales')
            paciente.antecedentesSociales = request.POST.get('antecedentesSociales')
            paciente.historiaPersonal = request.POST.get('historiaPersonal')
            paciente.impresionDiagnostica = request.POST.get('impresionDiagnostica')
            paciente.diagnostico = Diagnostico.objects.filter(id=request.POST.get('diagnostico')).first()
            paciente.analisis = request.POST.get('analisis')
            paciente.planTrabajo = request.POST.get('planTrabajo')
            paciente.save()
            messages.success(request, 'La información del paciente se guardo correctamente.', extra_tags='success')
        except Exception as e:
            saveLog(request.user, "No se pudo actualizar Paciente. Metodo PacienteUpdate", e)
            messages.error(request, 'No fue posible guardar la información del paciente.', extra_tags='danger')
        
        return redirect('main:PacienteList')

    return render(request, 'paciente/update.html', context)
