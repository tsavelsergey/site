from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


def index(request):
    return render(request, 'web/index.html')

def catalog(request):
    product = Product.objects.all()
    return render(request, 'web/catalog.html', {'pr': product})

# def catalog(request):
#     return render(request, 'web/catalog.html')

def info(request):
    return render(request, 'web/info.html')

def social(request):
    return render(request, 'web/social.html')

def description(request):
    product = Product.objects.all()
    return render(request, 'web/description.html', {'pr': product})
