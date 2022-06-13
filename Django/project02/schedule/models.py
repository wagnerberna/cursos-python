# from tkinter import CASCADE
from django.db import models
from patients.models import Patients

# importa chave estrangeira id pacientes
# permite deletar em cascata
# related name usado no serializers
class Schedule(models.Model):
    id_schedule = models.AutoField(primary_key=True)
    date_hour = models.DateTimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    id_patient = models.ForeignKey(
        Patients,
        on_delete=models.CASCADE,
        related_name="schedule",
        blank=False,
        null=False,
    )

    #  unique_toguether não permite agendamento no mesmo horário com o mesmo paciente (tupla com os campos)
    class Meta:
        managed = True
        db_table = "schedule"
        unique_together = ("date_hour", "id_patient")
