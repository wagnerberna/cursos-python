from re import S
from rest_framework import serializers
from schedule.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"
