from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("\033[93m"+f'User {username} logged in!'+"\033[0m")
            return redirect('home')  # Redirect after login
        else:
            print("\033[93m"+f'Login failed for user: {username}'+"\033[0m")
            messages.error(request,"Invalid credentials")
            return render(request, 'user/login.html')
    return render(request, 'user/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken!")
            return render(request, 'user/signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request,"User with this email exists!")
            return render(request, 'user/signup.html')
        if password!=password2:
            messages.error(request,"Your passwords did not match!")
            return render(request, 'user/signup.html')

        user = User.objects.create_user(username=username,email=email, password=password)
        print("\033[93m"+f'New user created: {user.username}'+"\033[0m")
        login(request, user)
        return redirect('home')
    return render(request, 'user/signup.html')

@login_required
def logout_view(request):
    print("\033[93m"+f'User logged out: {request.user.username}'+"\033[0m")
    logout(request)
    return redirect('login_view')