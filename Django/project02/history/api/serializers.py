from dataclasses import field
from rest_framework import serializers
from history.models import History
from images.api.serializers import ImagesHistorySerializer


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"


class HistoryDetailsSerializer(serializers.ModelSerializer):
    images = ImagesHistorySerializer(many=True, read_only=True)

    class Meta:
        models = History
        fields = [
            "id_history",
            "date",
            "prognostic",
            "pain_site",
            "pain_type",
            "diagnostic",
            "id_schedule",
            "images",
        ]
