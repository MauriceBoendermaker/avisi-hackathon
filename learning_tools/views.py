<<<<<<< Updated upstream
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
import json
from django.contrib.auth import authenticate
=======
from django.contrib.auth import authenticate, login
>>>>>>> Stashed changes
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from django.http import JsonResponse
>>>>>>> Stashed changes
=======
import json
from django.contrib.auth import authenticate
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from django.http import JsonResponse
>>>>>>> main
from django.shortcuts import render


def index(request):
<<<<<<< HEAD
<<<<<<< Updated upstream
    return render(request, "test.html" )
=======
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
            # User klopt, wordt ingelogd
            login(request, user)
            render(request, "index.html")
            # return JsonResponse({"message": "Student logged in successfully", "username": user.username})
        else:
            # Invalide login
            # return JsonResponse({"message": "Invalid username or password"}, status=400)
            print("Invalid username or password")
            return render(request, "index.html")
=======
    return render(request, "index.html")


@require_GET
def login(request):
    return render(request, "login.html")


@require_POST
def login(request):
    data = json.loads(request.body)
    Email = data.get('email')
    Password = data.get('password')

    user = authenticate(request, username=Email, password=Password)

    if user is not None:
        # User klopt, wordt ingelogd
        login(request, user)
        return JsonResponse({"message": "Student logged in successfully", "username": user.username})
    else:
        # Invalide login
        return JsonResponse({"message": "Invalid username or password"}, status=400)
>>>>>>> main


@require_POST
def logout(request):
    # Logic for logging out
    return JsonResponse({"message": "Logged out successfully"})
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> main
