from django.core.management.base import BaseCommand


def cargar_colores():

    from Juego.models import Color
    import json

    ubicacion_archivo_json = 'Juego/fixtures/Colores.json'
    with open(ubicacion_archivo_json) as json_datos:

        colores = json.load(json_datos)

        for key, value in colores.items():
            Color.objects.update_or_create(Nombre=key,
                                           Red=value[0],
                                           Green=value[1],
                                           Blue=value[2],
                                           Alpha=value[3],
                                           defaults={'Nombre': key})

        json_datos.close()


class Command(BaseCommand):

    def handle(self, *args, **options):
        cargar_colores()

