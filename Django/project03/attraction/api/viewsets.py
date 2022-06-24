import imp
from rest_framework import viewsets
from attraction.models import Attraction
from attraction.api.serializers import AttractionSerializer


class attractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
