from re import S
from rest_framework import serializers
from schedule.models import Schedule
from history.api.serializers import HistorySerializer


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


# não inclui o id do paciente pq já existe no serializer pacientes
# importar campo históricos
class ScheduleDetailsSerializer(serializers.ModelSerializer):
    history = HistorySerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = [
            "id_schedule",
            "date_hour",
            "created_at",
            "activated",
            "description",
            "history",
        ]
