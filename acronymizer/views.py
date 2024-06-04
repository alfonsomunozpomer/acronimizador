from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("EL ACRONIMIZADOR")

def definition(request, word):
    return HttpResponse(f'Definición de {word}')


def define(request, word):
    return HttpResponse(f'Enviar definición de {word}')

