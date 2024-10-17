import pytest
from faker import Faker
from model_bakery import baker

from doenca.forms.apresentacao import ApresentacaoForm

class TestApresentacaoForms:
    """Testes para os formulários de Apresentacao"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_apresentacao_create(self, init):
        """Teste para criação de Apresentacao"""
        form = ApresentacaoForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_apresentacao_form_invalid(self, init):
        """Teste para formulário inválido de Apresentacao"""
        form = ApresentacaoForm(data=self.invalid_data)
        assert form.is_valid() is False
