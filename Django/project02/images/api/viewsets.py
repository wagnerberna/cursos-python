from rest_framework import viewsets
from images.models import ImagesHistory
from images.api.serializers import ImagesHistorySerializer


class ImagesHistoryViewset(viewsets.ModelViewSet):
    queryset = ImagesHistory.objects.all()
    serializer_class = ImagesHistorySerializer
