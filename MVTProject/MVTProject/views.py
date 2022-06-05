from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def templateTest(self):
    
    nombre = 'Alexis'
    apellido = 'Cequeira'
    edad = 20
    fecha_nac = 13/7/2001

    diccionario = {'nombre': nombre, 'apellido':apellido, 'edad': edad, 'fecha_nac': fecha_nac}

    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)