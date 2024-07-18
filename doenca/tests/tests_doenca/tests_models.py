import pytest
from faker import Faker
from model_bakery import baker

from doenca.models import Doenca

class TestDoencaModels:
    """Testes para o model Doenca"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.doenca = baker.make(Doenca)

    def test_count_doenca(self, init):
        """Testa a quantidade de doenca"""
        assert Doenca.objects.all().count() == 1

    def test_soft_delete_doenca(self, init):
        """Testa o soft delete de doenca"""
        Doenca.objects.all().delete()
        assert Doenca.objects.filter(deleted=False).count() == 0

    def test_create_doenca(self, init):
        """Testa a criação de doenca"""
        assert self.doenca.id is not None

    def test_update_doenca(self, init):
        """Testa a atualização de doenca"""
        # TODO - Altere o campo e o valor
        self.doenca.save()
        self.doenca.campo = "valor"
        self.doenca.save()
        doenca = Doenca.objects.get(campo="valor")
        assert doenca.campo == "valor"
