from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    u = User.objects.get(username="Adel")
    print(u.check_password("anirtaziri19"))
    return render(request, "index.html")


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    
    elif request.method == "POST":
        Email = request.POST.get('email')
        Password = request.POST.get('password')

        user = authenticate(username="Adel", password="anirtaziri19")
        if user:
            login(request, user)
            render(request, "index.html")
        else:
            print("Invalid username or password")
            return render(request, "index.html")

    return render(request, "index.html")



