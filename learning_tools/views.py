from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render


def index(request):
    print(request.user)
    return render(request, "index.html")


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        print("yes")
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username="admin", password="admin123")
        if user:
            login(request, user)
            redirect("/index")
        else:
            return render(request, "index.html")

    return render(request, "index.html")


def logout(request):
    if request.method == "GET":
        return render(request, "login.html")
