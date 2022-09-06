from django.urls import path, include
from . import views

# teste referencia produto
urlpatterns = [path("teste/", views.index)]
