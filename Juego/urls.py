from django.urls import path

from Juego.views import (cargar_grilla_ajax,
                         realizar_jugada_ajax,
                         cargar_jugadas_ajax,
                         consultar_tiempo_espera_ajax, 
                         realizar_denuncia_ajax,
                         obtener_denuncia_ajax)
from . import views

urlpatterns = [
    path('', views.juego, name='Juego'),

    # Peticiones de AJAX
    path('ajax/Lienzo/', cargar_grilla_ajax),
    path('ajax/Jugada/', realizar_jugada_ajax),
    path('ajax/Jugadas/', cargar_jugadas_ajax),
    path('ajax/Denuncia/Realizar/', realizar_denuncia_ajax),
    path('ajax/Denuncia/Obtener/', obtener_denuncia_ajax),
    path('ajax/Espera/', consultar_tiempo_espera_ajax),

]
