from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def landpage(request):
    # return render(request, "Welcome to SaatStore")
    # return HttpResponse("Welcome to SaatStore")
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'landpage.html', context)


def details(request):
    return HttpResponse("Details of X")


def buy(request):
    return HttpResponse("Purchase")


def add_product(request):
    return HttpResponse("add_product")


def edit_product(request):
    return HttpResponse("edit_product")


def remove_product(request):
    return HttpResponse("remove_product")
