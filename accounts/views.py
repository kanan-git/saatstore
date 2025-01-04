from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as sign_in
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Profile


def profile(request):
    return HttpResponse("profile")


def dashboard(request):
    return HttpResponse("dashboard")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            sign_in(request, user)
            messages.success(request, f'Welcome, {user.username}')
            return redirect('products/products_list')
        else:
            messages.info(request, f'No match found')
    else:
        form = AuthenticationForm()
        # return render(request, 'accounts/authentication.html', {'selection': 'login'})
        return render(request, 'accounts/authentication.html', {'selection': form})


def register(request):
    return render(request, 'accounts/authentication.html', {'selection': 'register'})


def logout(request):
    return HttpResponse("logout")
