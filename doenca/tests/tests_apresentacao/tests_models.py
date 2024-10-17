import pytest
from faker import Faker
from model_bakery import baker

from doenca.models import Apresentacao

class TestApresentacaoModels:
    """Testes para o model Apresentacao"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.apresentacao = baker.make(Apresentacao)

    def test_count_apresentacao(self, init):
        """Testa a quantidade de apresentacao"""
        assert Apresentacao.objects.all().count() == 1

    def test_soft_delete_apresentacao(self, init):
        """Testa o soft delete de apresentacao"""
        Apresentacao.objects.all().delete()
        assert Apresentacao.objects.filter(deleted=False).count() == 0

    def test_create_apresentacao(self, init):
        """Testa a criação de apresentacao"""
        assert self.apresentacao.id is not None

    def test_update_apresentacao(self, init):
        """Testa a atualização de apresentacao"""
        # TODO - Altere o campo e o valor
        self.apresentacao.save()
        self.apresentacao.campo = "valor"
        self.apresentacao.save()
        apresentacao = Apresentacao.objects.get(campo="valor")
        assert apresentacao.campo == "valor"
