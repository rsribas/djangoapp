# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
#import django_tables2 as tables

class Support(models.Model):
	"""Abertura de Tickets para a o NOC"""
	assunto = models.CharField(max_length=200)
	descricao = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Devolve representacao em string do modelo"""
		return self.assunto

class Module(models.Model):
	"""Modulos disponiveis da aplicacao"""
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	CHOICE = (('Y','Yes'),('N','No'))
	builtin = models.CharField(max_length=1, choices=CHOICE, blank=True)
#	user = models.ForeignKey(User)

	def __str__(self):
		"""Devolve representacao em string"""
		return self.name
