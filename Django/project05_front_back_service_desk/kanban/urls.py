from django.urls import path

from kanban.views.views import about, home

urlpatterns = [path("", home), path("about/", about)]
