from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega3Trueba.models import *
from AppEntrega3Trueba.forms import *

#from AppEntrega3Trueba.models import Curso

# Create your views here.


def inicio(request):
    #return HttpResponse('Esta es la vista de bienvenida')
    return render(request,'AppEntrega3Trueba/inicio.html')


def jugadores(request):
        if request.method == 'POST':
            
            mi_formulario = JugadorFormulario(request.POST)
            print(mi_formulario)

            if mi_formulario.is_valid:
                 
                 
                informacion = mi_formulario.cleaned_data
      
                jugador = Jugador(nombre=informacion["nombre"], apellido=informacion["apellido"], alias=informacion["alias"], fecha_nacimiento=informacion["fecha_nacimiento"], edad=informacion["edad"], nacionalidad=informacion["nacionalidad"], posicion=informacion["posicion"], esta_retirado=informacion["esta_retirado"], goles=informacion["goles"], asistencias=informacion["asistencias"], cant_partidos=informacion["cant_partidos"], partidos_ganados=informacion["partidos_ganados"], partidos_empatados=informacion["partidos_empatados"], partidos_perdidos=informacion["partidos_perdidos"], palmares=informacion["palmares"] )
 
                jugador.save()
 
                return render(request, "AppEntrega3Trueba/inicio.html")
        
        else:

            mi_formulario = JugadorFormulario()
 
        return render(request,"AppEntrega3Trueba/jugadores.html", {'mi_formulario':mi_formulario})

def estadios(request):
    if request.method == 'POST':
            
            mi_formulario = EstadioFormulario(request.POST)
            print(mi_formulario)

            if mi_formulario.is_valid:
                 
                 
                informacion = mi_formulario.cleaned_data
      
                estadio = Estadio(nombre=informacion["nombre"], nombre_fant=informacion["nombre_fant"], capacidad=informacion["capacidad"], ubicacion=informacion["ubicacion"], club=informacion["club"], )

                estadio.save()
 
                return render(request, "AppEntrega3Trueba/inicio.html")
        
    else:
         mi_formulario = EstadioFormulario()
 
    return render(request,"AppEntrega3Trueba/estadios.html", {'mi_formulario':mi_formulario})

def clubes(request):
    if request.method == 'POST':
            
            mi_formulario = ClubFormulario(request.POST)
            print(mi_formulario)

            if mi_formulario.is_valid:
                 
                 
                informacion = mi_formulario.cleaned_data
      
                club = Club(nombre=informacion["nombre"], apodos=informacion["apodos"], socios=informacion["socios"], division=informacion["division"], fundacion=informacion["fundacion"], colores_principales=informacion["colores_principales"])

                club.save()
 
                return render(request, "AppEntrega3Trueba/inicio.html")
        
    else:
         mi_formulario = ClubFormulario()
 
    return render(request,"AppEntrega3Trueba/clubes.html", {'mi_formulario':mi_formulario})





def buscar_jugador(request):
     
     return render(request, 'AppEntrega3Trueba/buscarJugador.html')


def buscando_jugador(request):
     
     if request.GET['apellido']:
          apellido = request.GET['apellido']
          jugadores = Jugador.objects.filter(apellido__icontains=apellido)
     #respuesta = f'Buscando jugador con apellido {request.GET['apellido'] }'
          return render(request, 'AppEntrega3Trueba/resultadosBusquedaJugador.html', {'jugadores':jugadores, 'apellido':apellido})
     else:
          respuesta ="No se ha enviado ningún dato"

     return HttpResponse(respuesta)

def buscar_club(request):
     
     return render(request, 'AppEntrega3Trueba/buscarClub.html')

def buscando_club(request):
     if request.GET['nombre']:
          nombre = request.GET['nombre']
          clubes = Club.objects.filter(nombre__icontains=nombre)
          return render(request, 'AppEntrega3Trueba/resultadosBusquedaClub.html', {'clubes':clubes, 'nombre':nombre})
     else:
          respuesta ="No se ha enviado ningún dato"

     return HttpResponse(respuesta)


def buscar_estadio(request):
     
     return render(request, 'AppEntrega3Trueba/buscarEstadio.html')

def buscando_estadio(request):
     if request.GET['nombre_fant']:
          nombre_fant = request.GET['nombre_fant']
          estadios = Estadio.objects.filter(nombre_fant__icontains=nombre_fant)
          return render(request, 'AppEntrega3Trueba/resultadosBusquedaEstadio.html', {'estadios':estadios, 'nombre_fant':nombre_fant})
     else:
          respuesta ="No se ha enviado ningún dato"

     return HttpResponse(respuesta)

