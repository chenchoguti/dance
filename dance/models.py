from django.db import models
from django.contrib import admin
from django.utils import timezone

class Bailarina(models.Model):
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=60)
	descripcion = models.TextField()
	fecha_nacimiento = models.DateField()

	def __str__(self):
		return self.nombre

class Teatro(models.Model):
	nombre= models.CharField(max_length=60)
	historia = models.TextField()
	fecha_creacion = models.DateTimeField(
		default=timezone.now)
	bailarinas = models.ManyToManyField(Bailarina, through='Show')

	def __str__(self):
		return self.nombre


class Show(models.Model):
	#fecha = models.DateField()
	bailarina = models.ForeignKey(Bailarina, on_delete=models.CASCADE)

	teatro = models.ForeignKey(Teatro, on_delete=models.CASCADE)


class ShowInLine(admin.TabularInline):
	model = Show
	extra = 1

class BailarinaAdmin(admin.ModelAdmin):
	inlines= (ShowInLine,)

class TeatroAdmin(admin.ModelAdmin):
	inlines = (ShowInLine,)
	
