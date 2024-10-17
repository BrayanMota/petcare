from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)

from doenca.models import Apresentacao
from doenca.forms.apresentacao import ApresentacaoForm


# Views do Models Apresentacao
class ApresentacaoListView(BaseListView):
    """Classe para gerenciar a listagem do Apresentacao"""

    model = Apresentacao
    template_name = "doenca/apresentacao/apresentacao_list.html"
    context_object_name = "apresentacao"
    list_display = [
        "conteudo_imagem",
        "conteudo_texto",
        "doenca",
        "ordem",
        "tipo_conteudo",
    ]
    search_fields = [
        "conteudo_imagem",
        "conteudo_texto",
        "doenca",
        "ordem",
        "tipo_conteudo",
    ]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ApresentacaoListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(ApresentacaoListView, self).get_queryset()
        return queryset


class ApresentacaoDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Apresentacao"""

    model = Apresentacao
    form_class = ApresentacaoForm
    success_url = "doenca:apresentacao-list"
    template_name = "doenca/apresentacao/apresentacao_detail.html"
    context_object_name = "apresentacao"

    def get_context_data(self, **kwargs):
        context = super(ApresentacaoDetailView, self).get_context_data(**kwargs)
        return context


class ApresentacaoCreateView(BaseCreateView):
    """Classe para gerenciar o create do Apresentacao"""

    model = Apresentacao
    form_class = ApresentacaoForm
    context_object_name = "apresentacao"
    success_url = "doenca:apresentacao-list"
    template_name = "doenca/apresentacao/apresentacao_create.html"
    # inlines = []
    # form_modals = []


class ApresentacaoUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Apresentacao"""

    model = Apresentacao
    form_class = ApresentacaoForm
    context_object_name = "apresentacao"
    success_url = "doenca:apresentacao-list"
    template_name = "doenca/apresentacao/apresentacao_update.html"
    # inlines = []
    # form_modals = []


class ApresentacaoDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Apresentacao"""

    model = Apresentacao
    form_class = ApresentacaoForm
    context_object_name = "apresentacao"
    success_url = "doenca:apresentacao-list"
    template_name = "doenca/apresentacao/apresentacao_delete.html"


class ApresentacaoRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Apresentacao"""

    model = Apresentacao
    context_object_name = "apresentacao"
    success_url = "doenca:apresentacao-list"
    template_name = "doenca/apresentacao/apresentacao_restore.html"


# Fim das Views do Models Apresentacao
