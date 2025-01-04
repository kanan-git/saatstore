from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm


def landpage(request):
    products = Product.objects.all()
    # products = (
    #     {
    #         'id': 1,
    #         'title': 'iWatch',
    #         'brand': 'Apple',
    #         'category': 'digital',
    #         'description': 'Lorem ipsum sit dolor',
    #         'price': 1000.0,
    #         'availability': True,
    #         'image_path': '317-200x200.jpg',
    #     },
    #     {
    #         'id': 2,
    #         'title': 'NoName',
    #         'brand': 'DefButNotDefault',
    #         'category': 'classic',
    #         'description': 'Random text qwerty',
    #         'price': 1299.0,
    #         'availability': False,
    #         'image_path': '366-200x200.jpg',
    #     },
    #     {
    #         'id': 3,
    #         'title': 'Abc',
    #         'brand': 'DefButNotDefault',
    #         'category': 'military',
    #         'description': 'Say my name',
    #         'price': 2999.0,
    #         'availability': True,
    #         'image_path': '461-200x200.jpg',
    #     },
    #     {
    #         'id': 4,
    #         'title': 'Random_1',
    #         'brand': 'DefButNotDefault',
    #         'category': 'mechanical',
    #         'description': 'Dónde está la biblioteca?',
    #         'price': 899.0,
    #         'availability': False,
    #         'image_path': '857-200x200.jpg',
    #     },
    #     {
    #         'id': 5,
    #         'title': 'Random_2',
    #         'brand': 'CheapSheets',
    #         'category': 'digital',
    #         'description': 'Cheap? It\'s not cheap, it\'s economical!',
    #         'price': 200.0,
    #         'availability': True,
    #         'image_path': '893-200x200.jpg',
    #     },
    #     {
    #         'id': 6,
    #         'title': 'Random_3',
    #         'brand': 'MarkQ',
    #         'category': 'sport',
    #         'description': 'This isn\'t just a product. It\'s an experience.',
    #         'price': 9999.0,
    #         'availability': True,
    #         'image_path': '949-200x200.jpg',
    #     },
    # )
    context = {
        'products': products
    }
    return render(request, 'products/landpage.html', context)


def details(request, id):
    # form = Product.objects.get(id=id)
    form = get_object_or_404(Product, id=id)
    context = {
        'details': form
    }
    return render(request, 'products/details.html', context)


def buy(request):
    return render(request, 'products/buy.html')

@login_required
def add_product(request):
    # productsCount = ...
    if request.method == "POST":
        form = ProductForm(request.POST)
        # print(request.method)
        # print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('products/landpage')
    elif request.method == "GET":
        form = {
            'data': ProductForm()
        }
        # print(request.method)
        # print(form.is_valid())
        # print(request)
    return render(request, 'products/add_product.html', form)


def edit_product(request, pk):
    product = get_object_or_404(Product, id=pk) # pk - primary key
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products/details', product.id)
    else:
        form = ProductForm(instance=product)
        context = {
            'form': form
        }
    return render(request, 'products/edit_product.html', context)


def remove_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.delete()
    messages.success(request, 'Product successfully deleted.')
    return redirect('products/products_list')


def all_products(request):
    context = {
        'list': Product.objects.all(),
        'count': Product.objects.all().__len__()
    }
    return render(request, 'products/store.html', context)


def about(request):
    return render(request, 'products/about.html')


def contact(request):
    return render(request, 'products/contactus.html')
