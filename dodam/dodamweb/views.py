from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def shelf(request):
    context = {
    }
    return render(request, 'shelf.html', context)


def spec(request):
    searchWord = request.GET.get('title')
    context = {
    }
    return render(request, 'spec.html', context)