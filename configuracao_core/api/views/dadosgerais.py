from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from configuracao_core.models import DadosGerais
from configuracao_core.api.serializers.dadosgerais import DadosGeraisSerializer


class DadosGeraisViewAPI(ModelViewSet):
    """ Classe para gerenciar as requisições da API para POST, PUT, PATCH e DELETE

        A lista search_fields deve ser configurada com os campos do models que poderão ser utilizados para realizar
        buscas no models como por exemplo search=valor_a_ser_pesquisado

        Retorne apenas os campos desejados com o parâmetro fields=campo1,campo2
    """
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DadosGerais.objects.select_related().all()
    serializer_class = DadosGeraisSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = []
    ordering_fields = []


class DadosGeraisReadOnlyAPI(OptimizedQuerySetMixin, ReadOnlyModelViewSet):
    """ Classe para gerenciar as requisições da API GET com apenas leitura

        A lista search_fields deve ser configurada com os campos do models que poderão ser utilizados para realizar
        buscas no models como por exemplo search=valor_a_ser_pesquisado

        Retorne apenas os campos desejados com o parâmetro fields=campo1,campo2
    """
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DadosGerais.objects.select_related().all()
    serializer_class = DadosGeraisSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = []
    ordering_fields = []