from rest_framework import viewsets
from address.models import Address
from address.api.serializers import AddressSerializer


class addressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
