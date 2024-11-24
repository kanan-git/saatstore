from django.shortcuts import (render, redirect)
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm)
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Profile
# from .forms import ProfileForm


def login(request):
    ...

def logout(request):
    ...

def register(request):
    ...

def profile(request):
    ...
