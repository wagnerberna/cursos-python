from django.shortcuts import render

# Não precisa colocar o caminho completo templates/produto/index.html


def index(request):
    return render(request, "produto/index.html")
