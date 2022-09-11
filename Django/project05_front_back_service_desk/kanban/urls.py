from django.urls import path

from kanban.views import about, home

urlpatterns = [path("", home), path("about/", about)]
