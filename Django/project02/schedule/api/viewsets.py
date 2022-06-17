from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from schedule.models import Schedule
from schedule.api.serializers import ScheduleSerializer, ScheduleDetailsSerializer


# ordena pelo campo escolhido
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by("date_hour")
    serializer_class = ScheduleSerializer

    @action(detail=True, methods=["get"])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Schedule.objects.filter(pk=pk)
        self.serializer_class = ScheduleDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)

        print(serializer.data)
        return Response(serializer.data)
