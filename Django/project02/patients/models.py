from django.db import models

# Create your models here.

# chave primária com auto incremente
# name campo não pode ser nulo ou falso
class Patients(models.Model):
    id_patient = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    address_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    # manage true para podermos gerenciar a tabela
    # define o nome da tabela
    class Meta:
        managed = True
        db_table = "patients"
