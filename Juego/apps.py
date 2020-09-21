from django.apps import AppConfig



class JuegoConfig(AppConfig):
    name = 'Juego'

    def CrearColores(self):
        from .models import Color
        import json

        if Color.objects.count() != 0:
            ubicacion_archivo_json = 'static/Juego/json/Colores.json'
            json_datos = open(ubicacion_archivo_json)
            colores = json.load(json_datos)
            for key, value in colores.iteritems():
                color = Color.objects.create(Nombre=key, Red=value[0], Green=value[1], Blue=value[2], Alpha=value[3])
                color.save()            
            json_datos.close()

    #Todo lo que se encuentre en este metodo se ejecutará al iniciar el sitio, antes de que cualquiera acceda a este  
    def ready(self):
        pass

