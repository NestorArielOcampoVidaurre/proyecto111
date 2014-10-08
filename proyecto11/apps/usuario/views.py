#encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#para importar los campos de usuario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
def principal(request):
	return render_to_response("inicio.html",{},RequestContext(request))

def registro(request):
	if request.method=="POST":
		fusuario=UserCreationForm(request.POST)
		if fusuario.is_valid():
			fusuario.save()
			usuario=request.POST["username"]
			#buscando al usuario qe emos creado
			nuevo_usuario=User.objects.get(username=usuario)
			#creamos su perfil
			perfil=PerfilUser.objects.create(user=nuevo_usuario)
			return HttpResponse("registrado")
	else:
		fusuario=UserCreationForm()	
	return render_to_response("registro.html",{'formulario':fusuario},context_instance=RequestContext(request))	