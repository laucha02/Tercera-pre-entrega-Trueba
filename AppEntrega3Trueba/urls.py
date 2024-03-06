
from django.urls import path
from AppEntrega3Trueba.views import *

urlpatterns = [
    path('',inicio, name='Inicio'),
    path('jugadores/',jugadores, name='Jugadores'),
    path('estadios/',estadios,name='Estadios'),
    path('clubes/',clubes,name='Clubes'),
    #path('jugadoresFormulario/', jugadores_formulario, name="jugadoresFormulario"),
    #path('clubesFormulario/',clubes_formulario, name='clubesFormulario'),
    #path('estadiosFormulario/',estadios_formulario,name='estadiosFormulario'),
    path('buscarJugador/',buscar_jugador,name='buscarJugador'),
    path('buscandoJugador/',buscando_jugador),
    path('buscarClub/',buscar_club, name='buscarJugador'),
    path('buscandoClub/',buscando_club),
    path('buscarEstadio/',buscar_estadio,name='buscarEstadio'),
    path('buscandoEstadio/',buscando_estadio)


]