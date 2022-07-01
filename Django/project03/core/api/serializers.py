from email.headerregistry import Address
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import TouristSpot
from attraction.models import Attraction
from attraction.api.serializers import AttractionSerializer
from address.api.serializers import AddressSerializer
from reviews.api.serializers import ReviewsSerializer

# Nested Relationship (inclui info de outras tabelas usando outros serializers)
# many=True pode relação 1 p/ N
# read_only=True e read_only_fields torna os campos não obrigatórios
class TouristSpotSerializer(ModelSerializer):
    attraction = AttractionSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)
    reviews = ReviewsSerializer(many=True, read_only=True)
    # # Serializer Method Field
    description_complete = SerializerMethodField()

    class Meta:
        model = TouristSpot
        fields = (
            "id",
            "name",
            "description",
            "attraction",
            "address",
            "reviews",
            "description_complete",
            "description_complete_2",
        )
        read_only_fields = (
            "description",
            "attraction",
            "address",
            "reviews",
            "description_complete",
            "description_complete_2",
        )

    # Serializer Method Field (get_nomeCampo)
    # objeto dá acesso ao objeto completo para criar campos personalizados
    def get_description_complete(self, obj):
        return "%s - %s no bairro: %s" % (obj.name, obj.description, obj.address)


class TouristSpotAllSerializer(ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = "__all__"
