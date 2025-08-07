from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages


def login(request):
    return render(request, 'user/login.html')

def signup(request):
    return render(request, 'user/signup.html')


@login_required
def logout(request):
    return render(request, 'user/logout.html')