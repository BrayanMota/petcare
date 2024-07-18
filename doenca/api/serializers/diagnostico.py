
from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from doenca.models import Diagnostico


class DiagnosticoSerializer(FieldsListSerializerMixin, ModelSerializer):
    """ Class do serializer do model Diagnostico para o POST, PUT, PATCH, DELETE """
    class Meta:
        model = Diagnostico
        exclude = ["deleted", "enabled"]
