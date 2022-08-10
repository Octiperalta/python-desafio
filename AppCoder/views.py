from xml.dom.expatbuilder import FragmentBuilder
from django.template import loader
from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse


# Create your views here.
def familiares(request):
    familiares = Familiar.objects.all()
    print('Flia', familiares)
    # template = loader.get_template('familiares.html')
    # # return render(request, 'familiares.html', {""})

    # document = template.render(familiares)
    # return HttpResponse(document)
    return render(request, 'familiares.html', {'family': familiares})


def cargarFamiliares(request):
    nombres = [
        {"nombre": 'Juan', "edad": 20},
        {"nombre": 'Pedro', "edad": 50},
        {"nombre": 'Maria', "edad": 12}
    ]

    for x in nombres:
        print(x['nombre'])
        familiar = Familiar(nombre=x['nombre'],
                            apellido='Perez', edad=x['edad'])
        familiar.save()

    return HttpResponse('Familiares cargados!')
