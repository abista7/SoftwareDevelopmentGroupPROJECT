from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'about/index.html')


def arjun(request):
    return render(request, 'about/arjun.html')


def dylan(request):
    return render(request, 'about/dylan.html')


def mariam(request):
    return render(request, 'about/mariam.html')


def sawara(request):
    return render(request, 'about/sawara.html')


def ryan(request):
    return render(request, 'about/ryan.html')


def cassie(request):
    return render(request, 'about/cassie.html')
