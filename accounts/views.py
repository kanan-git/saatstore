from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile


def login(request):
    return HttpResponse("login")


def logout(request):
    return HttpResponse("logout")


def register(request):
    return HttpResponse("register")


def profile(request):
    return HttpResponse("profile")


def my_products(request):
    return HttpResponse("my products")
