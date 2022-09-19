from django.urls import include, path
from helpdesk.api.viesets import demandViewSet
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r"demand", demandViewSet)

urlpatterns = [
    path("demand/", include(route.urls)),
]
