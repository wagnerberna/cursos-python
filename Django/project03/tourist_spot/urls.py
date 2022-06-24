"""tourist_spot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# 2 imports para abrir as imagens:
from django.conf import settings
from django.conf.urls.static import static

# imports Token:
from rest_framework.authtoken.views import obtain_auth_token

from core.api.viewsets import (
    TouristSpotViewSet,
    TouristSpotAllViewSet,
    TouristSpotApprovedViewSet,
    TouristSpotQuerySetViewSet,
    TouristSpotTestListViewSet,
    TouristSpotTestActionViewSet,
    TouristSpotQueryStringViewSet,
    TouristSpotDjangoFilterViewSet,
    TouristSpotSearchFilterViewSet,
)
from address.api.viewsets import addressViewSet
from attraction.api.viewsets import attractionViewSet
from reviews.api.viewsets import ReviewsViewSet

# necessário add um basename para cada rota do mesmo viewset
router = routers.DefaultRouter()
router.register(r"touristspot", TouristSpotViewSet, basename="tourist_spot")
router.register(r"touristspotall", TouristSpotAllViewSet, basename="tourist_spot_all")
router.register(
    r"TouristSpotApproved", TouristSpotApprovedViewSet, basename="tourist_spot_Approved"
)
router.register(
    r"TouristSpotqueryset", TouristSpotQuerySetViewSet, basename="tourist_spot_queryset"
)

router.register(
    r"TouristSpotTestList",
    TouristSpotTestListViewSet,
    basename="tourist_spot_test_list",
)

router.register(
    r"TouristSpotTestAction",
    TouristSpotTestActionViewSet,
    basename="tourist_spot_test_ction",
)

router.register(
    r"TouristSpotQueryString",
    TouristSpotQueryStringViewSet,
    basename="Tourist_Spot_Query_String",
)

router.register(
    r"TouristSpotDjangoFilter",
    TouristSpotDjangoFilterViewSet,
    basename="Tourist_Spot_django_filter",
)

router.register(
    r"TouristSpotSearchFilter",
    TouristSpotSearchFilterViewSet,
    basename="Tourist_Spot_search_filter",
)

router.register(r"address", addressViewSet, basename="address")
router.register(r"attraction", attractionViewSet, basename="attraction")
router.register(r"reviews", ReviewsViewSet, basename="reviews")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-token-auth/", obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# config para abrir imagens (endereços settings):
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# URL token:
# path('api-token-auth/', views.obtain_auth_token)
