from rest_framework import viewsets
from patients.models import Patients
from patients.api.serializers import PatientsSerializer


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer
