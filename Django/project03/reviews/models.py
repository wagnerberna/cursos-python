from django.db import models
from django.contrib.auth.models import User

# importa os usuários do Django
# Se deletar o usuário deleta dos os comentários dele.
# max_digits=2 número máximo de dígitos incluindo as casas decimais
# decimal_places=1 uma casa decimal após a virgula
class Reviews(models.Model):
    id_review = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=False, null=False)
    ranking = models.DecimalField(max_digits=2, decimal_places=1)
    approved = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "reviews"

    # add na visualização do admin o username ou o primeiro nome
    def __str__(self):
        return self.user.username
        # return self.user.first_name
