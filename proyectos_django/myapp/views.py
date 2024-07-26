from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hola_mundo(request):
    print('hola mundo estoy desde el servidor de django')

    html = "<html><body>hola mundo desde el navegador, mi nombre es: Yurley </body></html>"
    return HttpResponse(html)
