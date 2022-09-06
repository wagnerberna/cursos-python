import imp
from django.shortcuts import render

# aponta para templates na pasta base
def index(request):
    return render(request, "home/index.html")
