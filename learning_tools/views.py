from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    u = User.objects.get(username="Adel")
    print(u.check_password(""))
    return render(request, "index.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    
    elif request.method == "POST":
        Email = request.POST.get('email')
        Password = request.POST.get('password')

        user = authenticate(email="", password="")
        print(user)
        if user:
            # User klopt, wordt ingelogd
            login(request, user)
            print(user.username)
            render(request, "index.html")
            # return JsonResponse({"message": "Student logged in successfully", "username": user.username})
        else:
            # Invalide login
            # return JsonResponse({"message": "Invalid username or password"}, status=400)
            print("Invalid username or password")
            return render(request, "index.html")
        
    return render(request, "index.html")


@require_POST
def logout(request):
    # Logic for logging out
    return JsonResponse({"message": "Logged out successfully"})

