from pickle import NONE
from ssl import ALERT_DESCRIPTION_USER_CANCELLED, AlertDescription
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente
from .forms import LibroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def publicaciones(request):
    return render(request,'paginas/publicaciones.html')



def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pacientes')
    return render(request,'pacientes/crear.html', {'formulario': formulario})

def editar(request,id):
    editarPaciente = Paciente.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=editarPaciente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('pacientes')
    return render(request,'pacientes/editar.html',{'formulario': formulario})

def eliminar(request, id):
    eliminarpaciente = Paciente.objects.get(id=id) 
    
    eliminarpaciente.delete()
    return redirect('pacientes')

@login_required

def pacientes(request):
    datospacientes = Paciente.objects.all().order_by('habitacion')
    return render(request,'pacientes/index.html', {'pacientes1': datospacientes})

def cerrar_sesion(request):
    logout(request)
    return redirect('/')
