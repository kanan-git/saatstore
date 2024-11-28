from django.shortcuts import render

from .models import Product

# Create your views here.
def landpage(request):
    return render(request, "Welcome to SaatStore")

def details(request):
    return render(request, "Details of X")

def buy(request):
    return render(request, "Purchase")
