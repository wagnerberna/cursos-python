import imp
from django.db import models

# from core.models import TouristSpot


class Attraction(models.Model):
    id_attraction = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()
    minimum_age = models.IntegerField()
    # id_tourist_spot = models.ForeignKey(
    #     TouristSpot,
    #     on_delete=models.CASCADE,
    #     blank=False,
    #     null=True,
    #     related_name="tourist_spot",
    # )

    class Meta:
        managed = True
        db_table = "attraction"

    # campo de identificação dentro do django admin
    def __str__(self):
        return self.name
