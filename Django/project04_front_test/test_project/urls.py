"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

# Import views incluir a home, pode ser feita como se fosse um app igual blog
# OU importada direto

# include("") referencia url das páginas filhas
# criar o arquivo urls dentro do app blog q é referenciado
# chama o caminho dentro do blog/urls
# http://127.0.0.1:8000/blog/

urlpatterns = [
    path("", views.index),
    # path("admin/", admin.site.urls),
    # path("blog/", include("blog.urls")),
    # path("produto/", include("produto.urls")),
]