from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(
        request, "ti/home.html", context={"title": "Sistemas TI: Kanban e Helpdesk"}
    )


def about(request):
    return HttpResponse("Sistema TI de Projetos Kanban")
