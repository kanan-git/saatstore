from django.shortcuts import (render, redirect)
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm


def landpage(request):
    # products = Product.objects.all()
    products = (
        {
            'id': 1,
            'title': 'iWatch',
            'brand': 'Apple',
            'category': 'digital',
            'description': 'Lorem ipsum sit dolor',
            'price': 1000.0,
            'availability': True,
            'image_path': '317-200x200.jpg',
        },
        {
            'id': 2,
            'title': 'NoName',
            'brand': 'DefButNotDefault',
            'category': 'classic',
            'description': 'Random text qwerty',
            'price': 1299.0,
            'availability': False,
            'image_path': '366-200x200.jpg',
        },
        {
            'id': 3,
            'title': 'Abc',
            'brand': 'DefButNotDefault',
            'category': 'military',
            'description': 'Say my name',
            'price': 2999.0,
            'availability': True,
            'image_path': '461-200x200.jpg',
        },
        {
            'id': 4,
            'title': 'Random_1',
            'brand': 'DefButNotDefault',
            'category': 'mechanical',
            'description': 'Dónde está la biblioteca?',
            'price': 899.0,
            'availability': False,
            'image_path': '857-200x200.jpg',
        },
        {
            'id': 5,
            'title': 'Random_2',
            'brand': 'CheapSheets',
            'category': 'digital',
            'description': 'Cheap? It\'s not cheap, it\'s economical!',
            'price': 200.0,
            'availability': True,
            'image_path': '893-200x200.jpg',
        },
        {
            'id': 6,
            'title': 'Random_3',
            'brand': 'MarkQ',
            'category': 'sport',
            'description': 'This isn\'t just a product. It\'s an experience.',
            'price': 9999.0,
            'availability': True,
            'image_path': '949-200x200.jpg',
        },
    )
    context = {
        'products': products
    }

    # if request.method == 'POST':
    #     form = ProductForm(request.data)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('landpage')
    #     print("its POST")
    # elif request.method == 'GET':
    #     print("its GET")
    
    return render(request, 'landpage.html', context)


def details(request):
    return render(request, 'details.html')


def buy(request):
    return render(request, 'buy.html')


def add_product(request):
    return render(request, 'add_product.html')


def edit_product(request):
    return render(request, 'edit_product.html')


# def remove_product(request):
#     return render(request, '.html')
