from django.core.management.base import BaseCommand

from Juego.models import Color
from django.core.serializers import deserialize
import json



class Command(BaseCommand):
    
    def handle(self, *args, **options):

        if Color.objects.all().count() < 149:
            ubicacion_archivo_json = 'Juego/fixtures/Colores.json'
            with open(ubicacion_archivo_json) as json_datos:
        
                colores = json.load(json_datos)

                for key, value in colores.items():
                    color = Color.objects.create(Nombre=key, Red=value[0], Green=value[1], Blue=value[2], Alpha=value[3])
                    if not Color.objects.filter(Nombre=key).exists():
                        color.save()                    

            json_datos.close()