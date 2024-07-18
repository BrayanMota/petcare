import pytest
from faker import Faker
from model_bakery import baker

from doenca.forms.diagnostico import DiagnosticoForm

class TestDiagnosticoForms:
    """Testes para os formulários de Diagnostico"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_diagnostico_create(self, init):
        """Teste para criação de Diagnostico"""
        form = DiagnosticoForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_diagnostico_form_invalid(self, init):
        """Teste para formulário inválido de Diagnostico"""
        form = DiagnosticoForm(data=self.invalid_data)
        assert form.is_valid() is False
