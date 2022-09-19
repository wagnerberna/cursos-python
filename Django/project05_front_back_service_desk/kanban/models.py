from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


# auto_now_add (atualiza apenas quando é inserido)
# auto_now (atualiza toda vez q é alterado)
# on_delete set_null (quando uma categoria for apagada o campo se torna nulo)
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return "Projeto: %s / Status: %s" % (self.name, self.status)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False)
    description = models.CharField(max_length=150)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


# usa tabela de usuários do Django
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return "%s / Time: %s" % (self.user_name, self.user_name)


# task_owner (pode ficar em branco(no formulário para salvar), e o valor padrão é None)
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    task_owner = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return "Tarefa: %s / Projeto: %s, Responsável: %s, Status: %s" % (
            self.name,
            self.project,
            self.task_owner,
            self.status,
        )
