
from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from doenca.models import Doenca


class DoencaSerializer(FieldsListSerializerMixin, ModelSerializer):
    """ Class do serializer do model Doenca para o POST, PUT, PATCH, DELETE """
    class Meta:
        model = Doenca
        exclude = ["deleted", "enabled"]
