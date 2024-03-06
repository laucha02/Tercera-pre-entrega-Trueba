from django.db import models

# Create your models here.


class Jugador(models.Model):

    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 60)
    alias = models.CharField(max_length = 60, null=True, blank=True) #NO ES OBLIGATORIO
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length = 60)
    posicion = models.CharField(max_length = 60, default=0)


    esta_retirado = models.BooleanField()
    goles = models.IntegerField()
    asistencias= models.IntegerField()
    cant_partidos = models.IntegerField()
    partidos_ganados = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)

    #imagen = models.ImageField(upload_to="media", null=True)
    palmares = models.TextField(default=0)
    



class Estadio(models.Model):

    nombre = models.CharField(max_length = 60)
    nombre_fant = models.CharField(max_length = 60)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length = 60)
    club = models.CharField(max_length = 60)


class Club(models.Model):

    nombre = models.CharField(max_length = 60)
    apodos = models.CharField(max_length = 60)
    socios = models.IntegerField()
    division = models.CharField(max_length = 60)
    fundacion = models.DateField()
    colores_principales = models.CharField(max_length = 60)