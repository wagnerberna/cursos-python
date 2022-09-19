from helpdesk.models import Demand
from rest_framework import serializers


class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = "__all__"
