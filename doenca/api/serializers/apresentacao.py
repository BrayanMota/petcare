
from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from doenca.models import Apresentacao


class ApresentacaoSerializer(FieldsListSerializerMixin, ModelSerializer):
    """ Class do serializer do model Apresentacao para o POST, PUT, PATCH, DELETE """
    class Meta:
        model = Apresentacao
        exclude = ["deleted", "enabled"]
