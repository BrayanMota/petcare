import pytest
from faker import Faker
from model_bakery import baker
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.conf import settings

from doenca.models import Diagnostico
from doenca.views.index import DoencaIndexTemplateView
from doenca.views.diagnostico import (
    DiagnosticoListView,
    DiagnosticoDetailView,
    DiagnosticoCreateView,
    DiagnosticoUpdateView,
    DiagnosticoDeleteView,
)
from django.contrib.messages.storage.fallback import FallbackStorage

class TestDiagnosticoViews:
    """Teste para as views do model Diagnostico"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste", email="teste@email.com.br", password="senha_padrao_deve_ser_mudada"
        )
        self.diagnostico = baker.make(Diagnostico)

    def test_diagnostico_list(self, init):
        """Teste para a view list."""
        url = reverse("doenca:diagnostico-list")
        request = self.factory.get(url)
        request.user = self.user
        response = DiagnosticoListView.as_view()(request)
        assert response.status_code == 200

    def test_diagnostico_detail(self, init):
        """Teste para a view detail."""
        url = reverse("doenca:diagnostico-detail", args={self.diagnostico.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = DiagnosticoDetailView.as_view()(request, pk=self.diagnostico.pk)
        assert response.status_code == 200

    def test_diagnostico_create(self, init):
        """Teste para a view create."""
        url = reverse("doenca:diagnostico-create")
        request = self.factory.get(url)
        request.user = self.user
        response = DiagnosticoCreateView.as_view()(request)
        assert response.status_code == 200

    def test_diagnostico_create_post(self, init):
        """Teste para a view create usando Post."""

        # TODO - Adicione campos
        data = {}
        url = reverse("doenca:diagnostico-create")
        request = self.factory.post(url)
        request.user = self.user
        response = DiagnosticoCreateView.as_view()(request, data=data)
        assert response.status_code == 200

    def test_diagnostico_update(self, init):
        """Teste para a view update."""
        url = reverse("doenca:diagnostico-update", args={self.diagnostico.pk})
        request = self.factory.put(url)
        request.user = self.user
        response = DiagnosticoUpdateView.as_view()(request, pk=self.diagnostico.pk)
        assert response.status_code == 200

    def test_diagnostico_delete(self, init):
        """Teste para a view delete."""
        url = reverse("doenca:diagnostico-delete", args={self.diagnostico.pk})
        request = self.factory.delete(url)
        setattr(request, "session", "session")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        request.user = self.user
        response = DiagnosticoDeleteView.as_view()(request, pk=self.diagnostico.pk)
        mensagem = list(messages)[0].extra_tags
        assert mensagem == "success"
        assert response.status_code == 302

    def test_diagnostico_queryset_superuser_status(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("doenca:diagnostico-list"))
        request.user = self.user
        response = DiagnosticoListView.as_view()(request)
        assert response.status_code == 200

    def test_diagnostico_queryset_superuser(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("doenca:diagnostico-list"))
        request.user = self.user
        response = DiagnosticoListView.as_view()(request)
        assert len(response.context_data["object_list"]) == 1

    def test_doenca_index(self, init):
        """Teste para a view index."""
        url = reverse("doenca:doenca-index")
        request = self.factory.get(url)
        request.user = self.user
        response = DoencaIndexTemplateView.as_view()(request)
        assert response.status_code == 200
