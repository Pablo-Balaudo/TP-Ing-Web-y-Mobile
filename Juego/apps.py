from django.apps import AppConfig


def cargar_colores():
    try:
        from Juego.models import Color
        from django.core.serializers import deserialize
        import json

        if Color.objects.all().count() < 149:
            ubicacion_archivo_json = 'Juego/fixtures/Colores.json'
            with open(ubicacion_archivo_json) as json_datos:

                colores = json.load(json_datos)

                for key, value in colores.items():
                    color = Color.objects.create(Nombre=key, Red=value[0], Green=value[1], Blue=value[2], Alpha=value[3])
                    if not Color.objects.filter(Nombre=key).exists():
                        color.save()

                json_datos.close()
    except NameError:
        print('Aun no se cargó el modelo de datos')


class JuegoConfig(AppConfig):
    name = 'Juego'

    # Todo lo que se encuentre en este metodo se ejecutará al iniciar el sitio, antes de que cualquiera acceda a este
    def ready(self):
        cargar_colores()
