#encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

# Create your views here.
def principal(request):
	return render_to_response("inicio.html",{},RequestContext(request))