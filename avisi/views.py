# add views for index with test.html

from django.shortcuts import render

def index(request):
    return render(request, "test.html" )

