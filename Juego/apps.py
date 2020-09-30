from django.apps import AppConfig
from django.db.utils import OperationalError


# Este metodo es para cargar los colores en la base de 
# datos, desde el archivo json de la carpeta fixtures
# def cargar_colores():
#
#     from Juego.models import Color
#     from django.core.serializers import deserialize
#     import json
#
#     if Color.objects.all().count() < 149:
#         ubicacion_archivo_json = 'Juego/fixtures/Colores.json'
#         with open(ubicacion_archivo_json) as json_datos:
#
#             colores = json.load(json_datos)
#
#             for key, value in colores.items():
#                 color = Color.objects.create(
#                     Nombre=key,
#                     Red=value[0],
#                     Green=value[1],
#                     Blue=value[2],
#                     Alpha=value[3])
#                 if not Color.objects.filter(Nombre=key).exists():
#                     color.save()
#
#             json_datos.close()
#

class JuegoConfig(AppConfig):
    name = 'Juego'

    # # Todo lo que se encuentre en este metodo se ejecutará
    # # al iniciar el sitio, antes de que cualquiera acceda a este
    # def ready(self):
    #
    #     try:
    #         cargar_colores()
    #     except OperationalError as ex:
    #         print('Aun no se cargó el modelo de datos')
    #
    #     # Este TRY es porque, al ejecutarse esto antes que las
    #     # propias migraciones, tira error cuando no existe una base
    #     # de datos, pues se puregunta por una tabla de Colores, que aun no existe
