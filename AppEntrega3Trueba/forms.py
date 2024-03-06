from django import forms

class JugadorFormulario(forms.Form):

    nombre = forms.CharField(max_length = 60)
    apellido = forms.CharField(max_length = 60)
    alias = forms.CharField(max_length = 60, required='False') #NO ES OBLIGATORIO
    fecha_nacimiento = forms.DateField()
    edad = forms.IntegerField()
    nacionalidad = forms.CharField(max_length = 60)
    posicion = forms.CharField(max_length = 60, )


    esta_retirado = forms.BooleanField()
    goles = forms.IntegerField()
    asistencias= forms.IntegerField()
    cant_partidos = forms.IntegerField()
    partidos_ganados = forms.IntegerField()
    partidos_empatados = forms.IntegerField()
    partidos_perdidos = forms.IntegerField()

    #imagen = forms.ImageField(upload_to="media", null=True)
    palmares = forms.CharField(max_length = 200)


class ClubFormulario(forms.Form):

    nombre = forms.CharField()
    apodos = forms.CharField()
    socios = forms.IntegerField()
    division = forms.CharField()
    fundacion = forms.DateField()
    colores_principales = forms.CharField()

    
class EstadioFormulario(forms.Form):
    nombre = forms.CharField()
    nombre_fant = forms.CharField()
    capacidad = forms.IntegerField()
    ubicacion = forms.CharField()
    club = forms.CharField()
