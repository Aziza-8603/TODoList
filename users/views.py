from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('tasks:home')
        else:
            return render(
                request,
                'registration/login.html',
                {'error': 'Username yoki parol noto‘g‘ri'}
            )

    return render(request, 'registration/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'registration/signup.html',
                {'error': 'Bu username band'}
            )

        User.objects.create_user(
            username=username,
            password=password
        )
        return redirect('users:login')

    return render(request, 'registration/signup.html')


def logout_view(request):
    logout(request)  
    return redirect('users:login')


