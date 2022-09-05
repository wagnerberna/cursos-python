from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
# return HttpResponse("Olá Mundo!")


def index(request):
    return render(request, "teste.html")
