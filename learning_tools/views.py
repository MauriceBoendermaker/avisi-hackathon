from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    
    elif request.method == "POST":
        Email = request.POST.get('email')
        Password = request.POST.get('password')

        user = authenticate(email="A", password="banaan455")
        if user:
            user_login(request, user)
            render(request, "index.html")
        else:
            return render(request, "index.html")
        
    return render(request, "index.html")


@require_POST
def logout(request):
    # Logic for logging out
    return JsonResponse({"message": "Logged out successfully"})

