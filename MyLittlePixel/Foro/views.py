from django.shortcuts import render

Posts_Test = [{'Autor': 'Twilight Sparkle',
               'Titulo': 'Intereses 1',
               'Contenido': 'Me gustan los libros',
               'Fecha_Publicacion': '21/08/2020'
               },
              {'Autor': 'Discord',
               'Titulo': 'Intereses 2',
               'Contenido': 'Me gusta trollear',
               'Fecha_Publicacion': '22/08/2020'}]


def foro(request):
    contenido = {'Posts': Posts_Test}
    return render(request, 'Foro/Foro.html', contenido)

