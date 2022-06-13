from tabnanny import verbose
from django.db import models

# Classe abastrata com 3 atributos
class Base(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
