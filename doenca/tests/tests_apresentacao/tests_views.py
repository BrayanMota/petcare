import pytest
from faker import Faker
from model_bakery import baker
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.conf import settings

from doenca.models import Apresentacao
from doenca.views.index import DoencaIndexTemplateView
from doenca.views.apresentacao import (
    ApresentacaoListView,
    ApresentacaoDetailView,
    ApresentacaoCreateView,
    ApresentacaoUpdateView,
    ApresentacaoDeleteView,
)
from django.contrib.messages.storage.fallback import FallbackStorage

class TestApresentacaoViews:
    """Teste para as views do model Apresentacao"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste", email="teste@email.com.br", password="senha_padrao_deve_ser_mudada"
        )
        self.apresentacao = baker.make(Apresentacao)

    def test_apresentacao_list(self, init):
        """Teste para a view list."""
        url = reverse("doenca:apresentacao-list")
        request = self.factory.get(url)
        request.user = self.user
        response = ApresentacaoListView.as_view()(request)
        assert response.status_code == 200

    def test_apresentacao_detail(self, init):
        """Teste para a view detail."""
        url = reverse("doenca:apresentacao-detail", args={self.apresentacao.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = ApresentacaoDetailView.as_view()(request, pk=self.apresentacao.pk)
        assert response.status_code == 200

    def test_apresentacao_create(self, init):
        """Teste para a view create."""
        url = reverse("doenca:apresentacao-create")
        request = self.factory.get(url)
        request.user = self.user
        response = ApresentacaoCreateView.as_view()(request)
        assert response.status_code == 200

    def test_apresentacao_create_post(self, init):
        """Teste para a view create usando Post."""

        # TODO - Adicione campos
        data = {}
        url = reverse("doenca:apresentacao-create")
        request = self.factory.post(url)
        request.user = self.user
        response = ApresentacaoCreateView.as_view()(request, data=data)
        assert response.status_code == 200

    def test_apresentacao_update(self, init):
        """Teste para a view update."""
        url = reverse("doenca:apresentacao-update", args={self.apresentacao.pk})
        request = self.factory.put(url)
        request.user = self.user
        response = ApresentacaoUpdateView.as_view()(request, pk=self.apresentacao.pk)
        assert response.status_code == 200

    def test_apresentacao_delete(self, init):
        """Teste para a view delete."""
        url = reverse("doenca:apresentacao-delete", args={self.apresentacao.pk})
        request = self.factory.delete(url)
        setattr(request, "session", "session")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        request.user = self.user
        response = ApresentacaoDeleteView.as_view()(request, pk=self.apresentacao.pk)
        mensagem = list(messages)[0].extra_tags
        assert mensagem == "success"
        assert response.status_code == 302

    def test_apresentacao_queryset_superuser_status(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("doenca:apresentacao-list"))
        request.user = self.user
        response = ApresentacaoListView.as_view()(request)
        assert response.status_code == 200

    def test_apresentacao_queryset_superuser(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("doenca:apresentacao-list"))
        request.user = self.user
        response = ApresentacaoListView.as_view()(request)
        assert len(response.context_data["object_list"]) == 1

    def test_doenca_index(self, init):
        """Teste para a view index."""
        url = reverse("doenca:doenca-index")
        request = self.factory.get(url)
        request.user = self.user
        response = DoencaIndexTemplateView.as_view()(request)
        assert response.status_code == 200
