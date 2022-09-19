from helpdesk.api.serializers import DemandSerializer
from helpdesk.models import Demand
from rest_framework import viewsets


class demandViewSet(viewsets.ModelViewSet):
    serializer_class = DemandSerializer
    queryset = Demand.objects.all()
