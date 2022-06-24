import imp
from rest_framework import viewsets
from history.api.serializers import HistorySerializer, HistoryDetailsSerializer
from history.models import History
from rest_framework.response import Response
from rest_framework.decorators import action


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all().order_by("date")
    serializer_class = HistorySerializer

    @action(detail=True, methods=["get"])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = History.objects.filter(pk=pk)
        self.serializer_class = HistoryDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
