from django.urls import path
from . import views

#  importa views do blog

# Create your views here.
# "" faz referência ao próprio blog, se colocar outro caminho fica no final do endereço
# index é o método que será chamado ao acessar o endereço entre aspas dentro do views
# chama o index dentro do blog/views

urlpatterns = [path("", views.index)]
