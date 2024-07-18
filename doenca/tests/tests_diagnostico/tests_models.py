import pytest
from faker import Faker
from model_bakery import baker

from doenca.models import Diagnostico

class TestDiagnosticoModels:
    """Testes para o model Diagnostico"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.diagnostico = baker.make(Diagnostico)

    def test_count_diagnostico(self, init):
        """Testa a quantidade de diagnostico"""
        assert Diagnostico.objects.all().count() == 1

    def test_soft_delete_diagnostico(self, init):
        """Testa o soft delete de diagnostico"""
        Diagnostico.objects.all().delete()
        assert Diagnostico.objects.filter(deleted=False).count() == 0

    def test_create_diagnostico(self, init):
        """Testa a criação de diagnostico"""
        assert self.diagnostico.id is not None

    def test_update_diagnostico(self, init):
        """Testa a atualização de diagnostico"""
        # TODO - Altere o campo e o valor
        self.diagnostico.save()
        self.diagnostico.campo = "valor"
        self.diagnostico.save()
        diagnostico = Diagnostico.objects.get(campo="valor")
        assert diagnostico.campo == "valor"
