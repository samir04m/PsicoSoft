from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import datetime
from .structures import *
from .functions import *
from .models import *

def Index(request):
    return redirect('main:PacienteList')

def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/pacientes')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username.lower(), password=password)
        if user:
            login(request, user)
            if not user.is_staff:
                psicologo = Psicologo.objects.filter(usuario=user).first()
                if not psicologo:
                    return redirect('main:CompletarRegistro')
            return redirect('main:PacienteList')
        else:
            messages.error(request, 'El usuario o la contraseña son incorrectos.', extra_tags='danger')
            return redirect('main:login')
    else:
        return render(request, 'usuario/login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña se cambio correctamente.', extra_tags='success')
            return redirect('main:change_password')
        else:
            messages.error(request, 'Corrige los errores para cambiar tu contraseña.', extra_tags='danger')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuario/change_password.html', {
        'form': form
    })

@login_required(login_url='/login/')
def CompletarRegistro(request):
    if request.method == 'POST':
        try:
            usuario = request.user
            usuario.first_name = request.POST.get('first_name').title()
            usuario.last_name = request.POST.get('last_name').title()
            usuario.save()
            psicologo = Psicologo(
                usuario = request.user,
                numeroTarjetaProfesional = request.POST.get('numeroTarjetaProfesional'),
                firma = request.FILES.get('firma'),
                logo = request.FILES.get('logo')
            )
            psicologo.save()
            messages.success(request, 'Tu registro se completo exitosamente.', extra_tags='success')
            return redirect('main:PacienteList')
        except Exception as e:
            saveLog(request.user, "No guardar informacion del psicologo. Metodo CompletarRegistro", e)
            messages.error(request, 'No fue posible guardar la información. Intente de nuevo.', extra_tags='danger')
            return redirect('main:CompletarRegistro')
    else:
        return render(request, 'usuario/completarRegistro.html')

@login_required(login_url='/login/')
def PacienteList(request):
    pacientes = Paciente.objects.filter(usuario = request.user).order_by('-id')
    context = {
        "pacientes": pacientes,
        "selectTipoDocumento": GetSelectTipoDocumento()
    }
    return render(request, 'paciente/list.html', context)

@login_required(login_url='/login/')
def PacienteCreate(request):
    if request.method == 'POST':
        tipoDocumento = request.POST.get('tipoDocumento')
        numeroDocumento = request.POST.get('numeroDocumento')
        if not existeDocumento(tipoDocumento, numeroDocumento):
            try:
                paciente = Paciente(
                    usuario = request.user,
                    nombres = request.POST.get('nombres').title(),
                    apellidos = request.POST.get('apellidos').title(),
                    tipoDocumento = tipoDocumento,
                    numeroDocumento = numeroDocumento,
                    fecha = datetime.now()
                )
                paciente.save()
                return redirect('main:PacienteUpdate', paciente.id)
            except Exception as e:
                saveLog(request.user, "No se pudo crear Paciente. Metodo PacienteCreate", e)
                messages.error(request, 'No fue posible crear el Paciente. Intente de nuevo.', extra_tags='danger')
        else:
            messages.error(request, 'Ya existe un paciente con este tipo y número de documento.', extra_tags='danger')
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
            paciente.nombres = request.POST.get('nombres').title()
            paciente.apellidos = request.POST.get('apellidos').title()
            paciente.tipoDocumento = request.POST.get('tipoDocumento')
            paciente.numeroDocumento = request.POST.get('numeroDocumento')
            paciente.fechaNacimiento = obtenerFecha(request.POST.get('fechaNacimiento'))
            paciente.sexo = request.POST.get('sexo')
            paciente.estadoCivil = request.POST.get('estadoCivil')
            paciente.direccion = request.POST.get('direccion').capitalize()
            paciente.celular = request.POST.get('celular')
            paciente.telefono = request.POST.get('telefono')
            paciente.nivelEducativo = request.POST.get('nivelEducativo').capitalize()
            paciente.ocupacion = request.POST.get('ocupacion').capitalize()
            paciente.motivoConsulta = request.POST.get('motivoConsulta').capitalize()
            paciente.antecedentesPersonales = request.POST.get('antecedentesPersonales').capitalize()
            paciente.antecedentesFamiliares = request.POST.get('antecedentesFamiliares').capitalize()
            paciente.antecedentesSociales = request.POST.get('antecedentesSociales').capitalize()
            paciente.historiaPersonal = request.POST.get('historiaPersonal').capitalize()
            paciente.impresionDiagnostica = request.POST.get('impresionDiagnostica').capitalize()
            paciente.diagnostico = getDiagnostico(request.POST.get('diagnostico'), request.POST.get('nuevoDiagnostico').capitalize())
            paciente.analisis = request.POST.get('analisis').capitalize()
            paciente.planTrabajo = request.POST.get('planTrabajo').capitalize()
            paciente.save()
            # raise ValueError("Exetion de prueba.")
            messages.success(request, 'La información del paciente se guardó correctamente.', extra_tags='success')
        except Exception as e:
            saveLog(request.user, "No se pudo actualizar Paciente. Metodo PacienteUpdate", e)
            messages.error(request, 'No fue posible guardar la información del paciente.', extra_tags='danger')
        
        return redirect('main:PacienteList')

    return render(request, 'paciente/update.html', context)

@login_required(login_url='/login/')
def PacienteEvolucion(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        try:
            evolucion = Evolucion(
                paciente = paciente,
                descripcion = request.POST.get('evolucion').capitalize(),
                fecha = datetime.now()
            )
            evolucion.save()
            messages.success(request, 'Se guardó la evolución del paciente.', extra_tags='success')
        except Exception as e:
            saveLog(request.user, "No se pudo guardar evolucion del Paciente. Metodo PacienteEvolucion", e)
            messages.error(request, 'No fue posible guardar la evolución del paciente.', extra_tags='danger')
        return redirect('main:PacienteList')
    
    return render(request, 'paciente/evolucion.html', {"paciente": paciente})

@login_required(login_url='/login/')
def PacienteDetails(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    context = {
        "paciente": paciente, 
        "psicologo": Psicologo.objects.filter(usuario=request.user).first(),
        "today": datetime.now()
    }
    print(paciente.evolucion_set.all())
    return render(request, 'paciente/details.html', context)