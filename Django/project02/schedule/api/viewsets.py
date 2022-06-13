from rest_framework import viewsets
from schedule.models import Schedule
from schedule.api.serializers import ScheduleSerializer

# ordena pelo campo escolhido
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by("date_hour")
    serializer_class = ScheduleSerializer
