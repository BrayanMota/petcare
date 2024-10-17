from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)

from doenca.models import Diagnostico
from doenca.forms.diagnostico import DiagnosticoForm


# Views do Models Diagnostico
class DiagnosticoListView(BaseListView):
    """Classe para gerenciar a listagem do Diagnostico"""

    model = Diagnostico
    template_name = "doenca/diagnostico/diagnostico_list.html"
    context_object_name = "diagnostico"
    list_display = ["descricao", "doenca", "nome", "testes"]
    search_fields = ["descricao", "doenca", "nome", "testes"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DiagnosticoListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(DiagnosticoListView, self).get_queryset()
        return queryset


class DiagnosticoDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Diagnostico"""

    model = Diagnostico
    form_class = DiagnosticoForm
    success_url = "doenca:diagnostico-list"
    template_name = "doenca/diagnostico/diagnostico_detail.html"
    context_object_name = "diagnostico"

    def get_context_data(self, **kwargs):
        context = super(DiagnosticoDetailView, self).get_context_data(**kwargs)
        return context


class DiagnosticoCreateView(BaseCreateView):
    """Classe para gerenciar o create do Diagnostico"""

    model = Diagnostico
    form_class = DiagnosticoForm
    context_object_name = "diagnostico"
    success_url = "doenca:diagnostico-list"
    template_name = "doenca/diagnostico/diagnostico_create.html"
    # inlines = []
    # form_modals = []


class DiagnosticoUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Diagnostico"""

    model = Diagnostico
    form_class = DiagnosticoForm
    context_object_name = "diagnostico"
    success_url = "doenca:diagnostico-list"
    template_name = "doenca/diagnostico/diagnostico_update.html"
    # inlines = []
    # form_modals = []


class DiagnosticoDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Diagnostico"""

    model = Diagnostico
    form_class = DiagnosticoForm
    context_object_name = "diagnostico"
    success_url = "doenca:diagnostico-list"
    template_name = "doenca/diagnostico/diagnostico_delete.html"


class DiagnosticoRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Diagnostico"""

    model = Diagnostico
    context_object_name = "diagnostico"
    success_url = "doenca:diagnostico-list"
    template_name = "doenca/diagnostico/diagnostico_restore.html"


# Fim das Views do Models Diagnostico
