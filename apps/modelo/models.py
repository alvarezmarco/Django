# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mascota (models.Model):
	nombre = models.CharField(max_length=30)
	sexo =  models.CharField(max_length=30)
	edad =  models.IntegerField()
	fecha_rescate= models.DateField()
	persona=models.ForeignKey('Persona', on_delete=models.CASCADE)
	vacuna = models.ManyToManyField('Vacuna')

class Persona (models.Model):
	
	dni = models.CharField(primary_key=True, max_length=15)
	nombre = models.CharField(max_length=50)
	apellidos =  models.CharField(max_length=70)
	edad =  models.IntegerField()
	telefono=models.CharField(max_length=15)
	domicilio = models.TextField()
	email= models.EmailField()

class Vacuna(models.Model):
	nombre_vac=models.CharField(max_length=50)

