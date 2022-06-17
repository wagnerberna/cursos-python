from rest_framework import viewsets
from history.api.serializers import HistorySerializer
from history.models import History


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all().order_by("date")
    serializer_class = HistorySerializer
