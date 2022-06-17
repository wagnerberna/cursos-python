from rest_framework import serializers
from patients.models import Patients
from schedule.api.serializers import ScheduleDetailsSerializer


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"


# importa o serializer detalhes da agenda q já têm o campo histórico
# many agenda pode ter vários registros para 1 só paciente
# read_only campo somente de leitura
class PatientsDetailsSerializer(serializers.ModelSerializer):
    schedule = ScheduleDetailsSerializer(many=True, read_only=True)

    # último campo se refere ao campo criado acima
    class Meta:
        model = Patients
        fields = [
            "id_patient",
            "name",
            "cpf",
            "birth_date",
            "address",
            "address_number",
            "created_at",
            "schedule",
        ]
