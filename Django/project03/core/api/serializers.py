from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import TouristSpot
from attraction.api.serializers import AttractionSerializer
from address.api.serializers import AddressSerializer
from reviews.api.serializers import ReviewsSerializer

# Nested Relationship
class TouristSpotSerializer(ModelSerializer):
    attraction = AttractionSerializer(many=True)
    address = AddressSerializer()
    reviews = ReviewsSerializer(many=True)

    class Meta:
        model = TouristSpot
        fields = ("id", "name", "description", "attraction", "address", "reviews")


class TouristSpotAllSerializer(ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = "__all__"
