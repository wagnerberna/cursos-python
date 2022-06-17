from django.db import models
from schedule.models import Schedule

# releated name nome relacionado com a listagem de históricos
class History(models.Model):
    id_history = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    prognostic = models.TextField(blank=True, null=True)
    pain_site = models.CharField(max_length=100, blank=True, null=True)
    pain_type = models.CharField(max_length=100, blank=True, null=True)
    diagnostic = models.TextField(blank=True, null=True)
    id_schedule = models.ForeignKey(
        Schedule,
        related_name="history",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    class Meta:
        managed = True
        db_table = "history"
