from dataclasses import field
from rest_framework import serializers
from images.models import ImagesHistory


class ImagesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesHistory
        fields = "__all__"
