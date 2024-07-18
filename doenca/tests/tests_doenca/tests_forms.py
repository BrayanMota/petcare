import pytest
from faker import Faker
from model_bakery import baker

from doenca.forms.doenca import DoencaForm

class TestDoencaForms:
    """Testes para os formulários de Doenca"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_doenca_create(self, init):
        """Teste para criação de Doenca"""
        form = DoencaForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_doenca_form_invalid(self, init):
        """Teste para formulário inválido de Doenca"""
        form = DoencaForm(data=self.invalid_data)
        assert form.is_valid() is False
