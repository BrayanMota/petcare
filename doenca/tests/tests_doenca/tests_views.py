import pytest
from faker import Faker
from model_bakery import baker
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.conf import settings

from doenca.models import Doenca
from doenca.views.index import DoencaIndexTemplateView
from doenca.views.doenca import (
    DoencaListView,
    DoencaDetailView,
    DoencaCreateView,
    DoencaUpdateView,
    DoencaDeleteView,
)
from django.contrib.messages.storage.fallback import FallbackStorage

class TestDoencaViews:
    """Teste para as views do model Doenca"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste", email="teste@email.com.br", password="senha_padrao_deve_ser_mudada"
        )
        self.doenca = baker.make(Doenca)

    def test_doenca_list(self, init):
        """Teste para a view list."""
        url = reverse("doenca:doenca-list")
        request = self.factory.get(url)
        request.user = self.user
        response = DoencaListView.as_view()(request)
        assert response.status_code == 200

    def test_doenca_detail(self, init):
        """Teste para a view detail."""
        url = reverse("doenca:doenca-detail", args={self.doenca.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = DoencaDetailView.as_view()(request, pk=self.doenca.pk)
        assert response.status_code == 200

    def test_doenca_create(self, init):
        """Teste para a view create."""
        url = reverse("doenca:doenca-create")
        request = self.factory.get(url)
        request.user = self.user
        response = DoencaCreateView.as_view()(request)
        assert response.status_code == 200

    def test_doenca_create_post(self, init):
        """Teste para a view create usando Post."""

        # TODO - Adicione campos
        data = {}
        url = reverse("doenca:doenca-create")
        request = self.factory.post(url)
        request.user = self.user
        response = DoencaCreateView.as_view()(request, data=data)
        assert response.status_code == 200

    def test_doenca_update(self, init):
        """Teste para a view update."""
        url = reverse("doenca:doenca-update", args={self.doenca.pk})
        request = self.factory.put(url)
        request.user = self.user
        response = DoencaUpdateView.as_view()(request, pk=self.doenca.pk)
        assert response.status_code == 200

    def test_doenca_delete(self, init):
        """Teste para a view delete."""
        url = reverse("doenca:doenca-delete", args={self.doenca.pk})
        request = self.factory.delete(url)
        setattr(request, "session", "session")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        request.user = self.user
        response = DoencaDeleteView.as_view()(request, pk=self.doenca.pk)
        mensagem = list(messages)[0].extra_tags
        assert mensagem == "success"
        assert response.status_code == 302

    def test_doenca_queryset_superuser_status(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("doenca:doenca-list"))
        request.user = self.user
        response = DoencaListView.as_view()(request)
        assert response.status_code == 200

    def test_doenca_queryset_superuser(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("doenca:doenca-list"))
        request.user = self.user
        response = DoencaListView.as_view()(request)
        assert len(response.context_data["object_list"]) == 1

    def test_doenca_index(self, init):
        """Teste para a view index."""
        url = reverse("doenca:doenca-index")
        request = self.factory.get(url)
        request.user = self.user
        response = DoencaIndexTemplateView.as_view()(request)
        assert response.status_code == 200
