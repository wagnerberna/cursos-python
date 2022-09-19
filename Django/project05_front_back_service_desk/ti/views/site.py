from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    # return render(request, "global/home.html")
    return render(request, "ti/pages/home.html", context={"title": "Home"})


def about(request):
    # return HttpResponse("Sistema TI de Kanban e Helpdesk")
    return render(
        request,
        "ti/pages/about.html",
        context={"title": "Sistemas TI: Kanban e Helpdesk"},
    )
