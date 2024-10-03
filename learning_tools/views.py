import json
from django.contrib.auth import authenticate
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
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


@require_POST
def logout(request):
    # Logic for logging out
    return JsonResponse({"message": "Logged out successfully"})
