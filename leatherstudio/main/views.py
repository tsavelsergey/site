from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    return HttpResponse("<h4>catalog</4>")
