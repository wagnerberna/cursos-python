from django.urls import path

from helpdesk.views import about, home

urlpatterns = [path("", home), path("about/", about)]
