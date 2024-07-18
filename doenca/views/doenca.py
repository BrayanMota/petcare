from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)

from doenca.models import Doenca
from doenca.forms.doenca import DoencaForm



# Views do Models Doenca
class DoencaListView(BaseListView):
    """Classe para gerenciar a listagem do Doenca"""
    model = Doenca
    template_name = "doenca/doenca/doenca_list.html"
    context_object_name = "doenca"
    list_display = ['causas', 'descricao', 'nome', 'sintomas', 'tratamentos']
    search_fields = ['causas', 'descricao', 'nome', 'sintomas', 'tratamentos']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DoencaListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(DoencaListView, self).get_queryset()
        return queryset


class DoencaDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Doenca """
    model = Doenca
    form_class = DoencaForm
    success_url = "doenca:doenca-list"
    template_name = "doenca/doenca/doenca_detail.html"
    context_object_name = "doenca"

    def get_context_data(self, **kwargs):
        context = super(DoencaDetailView, self).get_context_data(**kwargs)
        return context


class DoencaCreateView(BaseCreateView):
    """Classe para gerenciar o create do Doenca """
    model = Doenca
    form_class = DoencaForm
    context_object_name = "doenca"
    success_url = "doenca:doenca-list"
    template_name = "doenca/doenca/doenca_create.html"
    # inlines = []
    # form_modals = []


class DoencaUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Doenca """
    model = Doenca
    form_class = DoencaForm
    context_object_name = "doenca"
    success_url = "doenca:doenca-list"
    template_name = "doenca/doenca/doenca_update.html"
    # inlines = []
    # form_modals = []


class DoencaDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Doenca """
    model = Doenca
    form_class = DoencaForm
    context_object_name = "doenca"
    success_url = "doenca:doenca-list"
    template_name = "doenca/doenca/doenca_delete.html"


class DoencaRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Doenca """
    model = Doenca
    context_object_name = "doenca"
    success_url = "doenca:doenca-list"
    template_name = "doenca/doenca/doenca_restore.html"

# Fim das Views do Models Doenca
