import imp
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

# token e auth
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions,
)
from rest_framework.authentication import TokenAuthentication

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from core.models import TouristSpot
from core.api.serializers import TouristSpotSerializer, TouristSpotAllSerializer

# token de autenticação
# permissão por classe:
# isAdminUser (permite apenas admins)
# DjangoModelPermissions (permissões definidas na config. de user no Django admin)
# IsAuthenticatedOrReadOnly (acesso somente leitura Get sem token, com token escrita)
# IsAuthenticated (somente com token autenticado)
class TouristSpotViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer

    # permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)


class TouristSpotAllViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotAllSerializer


# Filter
# buscar apenas os aprovados 1 única filtragem
class TouristSpotApprovedViewSet(ModelViewSet):
    queryset = TouristSpot.objects.filter(approved=True)
    serializer_class = TouristSpotAllSerializer


# Filter + get_queriset
# método get queryset para várias filtragens no model
class TouristSpotQuerySetViewSet(ModelViewSet):
    serializer_class = TouristSpotAllSerializer

    def get_queryset(self):
        return TouristSpot.objects.filter(approved=True)


# modificar método nativo Django criando respostas personalizadas
# create(), retrieve(), update(), partial_update(),
# destroy() and list()
class TouristSpotTestListViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotAllSerializer

    def list(self, request, *args, **kwargs):
        return Response({"teste": "teste lista"})

    def create(self, request, *args, **kwargs):
        print(request.data)
        print(request.data["name"])
        # caso não encontre a chave retorna padrão
        print(request.data.get("name", "chave não encrontada"))
        print(request.data.get("nome", "chave não encrontada"))
        return Response({"add": request.data["name"]})

    def destroy(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass


# action
class TouristSpotTestActionViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotAllSerializer

    # action details True passa a PK
    @action(methods=["get"], detail=True)
    def TestAction(self, request, *args, **kwargs):
        print(kwargs)
        print(kwargs.get("pk"))
        key = kwargs.get("pk")
        return Response({"chave": key})


# get_queryset (query string)
# Filtro por query string enviada no end. do get
class TouristSpotQueryStringViewSet(ModelViewSet):
    serializer_class = TouristSpotAllSerializer
    # queryset = TouristSpot.objects.all()

    # url com espaços ele converte automaticamente
    # http://localhost:8000/TouristSpotQueryString/?id=1&name=Ponto A&description=bla bla bla
    # http://localhost:8000/TouristSpotQueryString/?id=1&name=Ponto%20A&description=bla%20bla%20bla
    # __iexact (torna case insensitive não importa letra maiúscula ou min.)
    # parametros opcionais, caso não seja passado retorna None
    def get_queryset(self):
        queryset = TouristSpot.objects.all()
        print(self.request)
        print(self.request.query_params)
        id = self.request.query_params.get("id", None)
        name = self.request.query_params.get("name__iexact", None)
        description = self.request.query_params.get("description__iexact", None)
        print(id, name, description)
        # primeiro define o query set para buscar todos, é um pré select all

        # define as buscas em cascata se os param. foram passados:
        if id:
            queryset = TouristSpot.objects.filter(pk=id)

        if name:
            queryset = TouristSpot.objects.filter(name=name)

        if description:
            queryset = TouristSpot.objects.filter(description=description)

        # return Response(queryset)
        # return queryset
        return queryset


# DjangoFilter / OrderingFilter
# Django Filtro por ordem ou campo (cria a query string)
# ver filtro por campo não funcionou
# Sem especificar os campos todos os campos aparecem no filtro
class TouristSpotDjangoFilterViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotAllSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["name", "description"]
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ["name", "description"]


# SearchFilter ("=" é o default)
# http://localhost:8000/TouristSpotSearchFilter/?search=pinho

# lookup_field altera o padrão de busca após a barra de id para campo x
# ao invés de esperar o id vai esperar uma string
# Têm de ser um campo único
# http://localhost:8000/TouristSpotSearchFilter/Ponto%20A/
# '^': 'istartswith',
# '=': 'iexact',
# '@': 'search',
# '$': 'iregex',
# tabela estrangeira "nomeCampo__nomeCampoTabelaEstrangeira
class TouristSpotSearchFilterViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotAllSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "description", "address__district"]
    lookup_field = "name"
