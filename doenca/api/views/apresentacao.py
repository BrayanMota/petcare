from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from doenca.models import Apresentacao
from doenca.api.serializers.apresentacao import ApresentacaoSerializer


class ApresentacaoViewAPI(ModelViewSet):
    """Classe para gerenciar as requisições da API para POST, PUT, PATCH e DELETE

    A lista search_fields deve ser configurada com os campos do models que poderão ser utilizados para realizar
    buscas no models como por exemplo search=valor_a_ser_pesquisado

    Retorne apenas os campos desejados com o parâmetro fields=campo1,campo2
    """

    # authentication_classes = [
    #     JWTAuthentication,
    #     SessionAuthentication,
    #     BasicAuthentication,
    # ]
    # permission_classes = [IsAuthenticated]
    queryset = Apresentacao.objects.select_related().all()
    serializer_class = ApresentacaoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["doenca__id", "topico"]
    ordering_fields = ["ordem"]

    def get_queryset(self):
        queryset = super().get_queryset()
        # Verificar se há um parâmetro 'doenca' na URL
        doenca_id = self.request.query_params.get("doenca", None)
        topico = self.request.query_params.get("topico", None)
        if doenca_id and topico:
            # Filtrar as apresentações relacionadas à doença
            queryset = queryset.filter(doenca__id=doenca_id, topico=topico)
        return queryset


class ApresentacaoReadOnlyAPI(OptimizedQuerySetMixin, ReadOnlyModelViewSet):
    """Classe para gerenciar as requisições da API GET com apenas leitura

    A lista search_fields deve ser configurada com os campos do models que poderão ser utilizados para realizar
    buscas no models como por exemplo search=valor_a_ser_pesquisado

    Retorne apenas os campos desejados com o parâmetro fields=campo1,campo2
    """

    # authentication_classes = [
    #     JWTAuthentication,
    #     SessionAuthentication,
    #     BasicAuthentication,
    # ]
    # permission_classes = [IsAuthenticated]
    queryset = Apresentacao.objects.select_related().all()
    serializer_class = ApresentacaoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["doenca__id", "topico"]
    ordering_fields = ["ordem"]

    def get_queryset(self):
        queryset = super().get_queryset()
        # Verificar se há um parâmetro 'doenca' na URL
        doenca_id = self.request.query_params.get("doenca", None)
        topico = self.request.query_params.get("topico", None)
        if doenca_id and topico:
            # Filtrar as apresentações relacionadas à doença
            queryset = queryset.filter(doenca__id=doenca_id, topico=topico)
        return queryset
