from django.db import models

# Create your models here.
class Lugar(models.Model):
	nombre = models.CharField(max_length=200)
   	descripcion = models.CharField(max_length=255)
   	direccion = models.CharField(max_length=255)
	latitud = models.DecimalField(max_digits=12, decimal_places=8)
	longitud = models.DecimalField(max_digits=12, decimal_places=8)
	def __unicode__(self):
		return self.nombre


class Lugar(models.Model):
	nombre = models.CharField(max_length=200)
   	descripcion = models.CharField(max_length=255)
   	direccion = models.CharField(max_length=255)
	latitud = models.DecimalField(max_digits=12, decimal_places=8)
	longitud = models.DecimalField(max_digits=12, decimal_places=8)
	def __unicode__(self):
		return self.nombre

class Comentario(models.Model):
	comentario = models.CharField(max_length=355)
	lugar = models.ForeignKey(Lugar)
	def __unicode__(self):
		return self.comentario

class Categoria(models.Model):
	nombre = models.CharField(max_length=255)
	def __unicode__(self):
		return self.nombre


class CategoriaLugar(models.Model):
	categoria = models.ForeignKey(Categoria)
	lugar = models.ForeignKey(Lugar)
		

