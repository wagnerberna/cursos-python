from django.contrib import admin
from django.urls import include, path

from ti.views.site import about, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", about),
    # path("helpdesk/", include("helpdesk.urls", namespace="helpdesk")),
    path("helpdesk/", include("helpdesk.urls")),
    path("kanban/", include("kanban.urls")),
    path("kanban/api/", include("kanban.api.urls")),
    path("helpdesk/api/", include("helpdesk.api.urls")),
]
