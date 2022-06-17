from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from patients.models import Patients
from patients.api.serializers import PatientsSerializer, PatientsDetailsSerializer


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

    # passa se deve ter os detalhes, e os métodos HTTP
    # filtrando pelo registro pk
    # serializer.data retorna todos registros vindos da queryset
    @action(detail=True, methods=["get"])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Patients.objects.filter(pk=pk)
        self.serializer_class = PatientsDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)

        print(serializer.data)
        return Response(serializer.data)
