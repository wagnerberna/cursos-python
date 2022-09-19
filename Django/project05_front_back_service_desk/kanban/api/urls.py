from django.urls import include, path
from kanban.api.viesets import ProjectViewSet
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r"project", ProjectViewSet)

urlpatterns = [
    path("project/", include(route.urls)),
]
