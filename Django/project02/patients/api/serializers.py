from rest_framework import serializers
from patients.models import Patients


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"
