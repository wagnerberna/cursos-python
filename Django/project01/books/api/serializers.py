from rest_framework import serializers
from books.models import Books

# serializer converte os dados para um formato padrão do python
# model define qual model vai ser utilizada
# fields Lista ou Tupla dos nomes dos campos, permite escolher campos que serão "serializados"
# all se todos forem usados
# Classe recebe dois atributos como padrão(model e fields)
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"
        # fields = [
        #     "id_book",
        #     "title",
        #     "author",
        #     "release_year",
        #     "state",
        #     "pages",
        #     "publishing_company",
        #     "create_at",
        # ]
