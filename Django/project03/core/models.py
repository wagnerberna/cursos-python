from django.db import models
from attraction.models import Attraction
from reviews.models import Reviews
from address.models import Address

# "images" pasta onde será salvo, (settigns-MEDIA_ROOT)
class TouristSpot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    attraction = models.ManyToManyField(Attraction, null=True, blank=True)
    reviews = models.ManyToManyField(Reviews, null=True, blank=True)

    class Meta:
        managed = True
        db_table = "tourist_spot"

    # campo de identificação dentro do django admin
    def __str__(self):
        return self.name

    # semelhante ao Serializer Method Field outra forma de fazer
    @property
    def description_complete_2(self):
        return "%s - %s no bairro: %s" % (self.name, self.description, self.address)
