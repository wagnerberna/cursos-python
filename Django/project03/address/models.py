from django.db import models
from django.forms import CharField

# Create your models here.
class Address(models.Model):
    id_address = models.AutoField(primary_key=True)
    street = models.CharField(max_length=150, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        managed = True
        db_table = "address"

    def __str__(self):
        return self.district
