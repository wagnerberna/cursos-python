from django.urls import path

from kanban.views import home

urlpatterns = [path("", home)]
