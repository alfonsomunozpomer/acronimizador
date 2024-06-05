from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Submission

def index(request):
    latest_definitions = Submission.objects.filter(status='A').order_by('word').order_by('-sent_date')
    context = {
        'latest_definitions_list': latest_definitions,
    }
    return render(request, 'acronymizer/index.html', context)

def definition(request, word):
    definition_list = get_list_or_404(Submission, word=word, status='A')
    context = {
        'word': word,
        'definition_list': definition_list
    }
    return render(request, 'acronymizer/detail.html', context)


def define(request, word):
    return HttpResponse(f'Enviar definición de {word}')

