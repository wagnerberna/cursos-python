import imp
from rest_framework import viewsets
from books.api.serializers import BooksSerializer
from books.models import Books

# viewsets são controllers ou recursos
# importa o serializer e o models para pegar todos objetos ou aplicar filtro
class BooksViewSets(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
    # queryset = Books.objects.filter(pk=pk)
