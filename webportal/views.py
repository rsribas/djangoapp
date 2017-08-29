# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from .models import Support
from .forms import SupportForm

#!python
#log/views.py
#from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")

@login_required(login_url="login/")
def devices(request):
	return render(request,"devices.html")

def support_topics(request):
  return render(request, 'support_topics.html', {'obj': Support.objects.all()})

#def support_topics(request):
#	"""Mostra os Meus Tickets"""
#	assunto = Support.objects.order_by('date_added')
#	context = {'assunto': assunto}
#	return render(request, 'support_topics.html', context)

def support_new(request):
	"""Adiciona novo ticket"""
	if request.method != 'POST':
		#Nenhum dado submetido; cria um formulario em branco
		form = SupportForm()
	else:
		#Dados de POST submetidos; processa os dados
		form = SupportForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('support_topics'))

	context = {'form': form}
	return render(request, 'support_new.html', context)
