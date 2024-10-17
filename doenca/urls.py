from doenca.views.index import DoencaIndexTemplateView
from django.urls import path, include

app_name = "doenca"
urlpatterns = [
    path("doenca/", DoencaIndexTemplateView.as_view(), name="doenca-index"),
]

from doenca.views.doenca import (
    DoencaCreateView,
    DoencaDetailView,
    DoencaDeleteView,
    DoencaListView,
    DoencaRestoreView,
    DoencaUpdateView,
)

# URLs do Models Doenca
urlpatterns += [
    path("doenca/doenca/", DoencaListView.as_view(), name="doenca-list"),
    path("doenca/doenca/create/", DoencaCreateView.as_view(), name="doenca-create"),
    path("doenca/doenca/<uuid:pk>/", DoencaDetailView.as_view(), name="doenca-detail"),
    path(
        "doenca/doenca/update/<uuid:pk>/",
        DoencaUpdateView.as_view(),
        name="doenca-update",
    ),
    path(
        "doenca/doenca/delete/<uuid:pk>/",
        DoencaDeleteView.as_view(),
        name="doenca-delete",
    ),
    path(
        "doenca/doenca/restore/<uuid:pk>/",
        DoencaRestoreView.as_view(),
        name="doenca-restore",
    ),
]
from doenca.views.diagnostico import (
    DiagnosticoCreateView,
    DiagnosticoDetailView,
    DiagnosticoDeleteView,
    DiagnosticoListView,
    DiagnosticoRestoreView,
    DiagnosticoUpdateView,
)

# URLs do Models Diagnostico
urlpatterns += [
    path("doenca/diagnostico/", DiagnosticoListView.as_view(), name="diagnostico-list"),
    path(
        "doenca/diagnostico/create/",
        DiagnosticoCreateView.as_view(),
        name="diagnostico-create",
    ),
    path(
        "doenca/diagnostico/<uuid:pk>/",
        DiagnosticoDetailView.as_view(),
        name="diagnostico-detail",
    ),
    path(
        "doenca/diagnostico/update/<uuid:pk>/",
        DiagnosticoUpdateView.as_view(),
        name="diagnostico-update",
    ),
    path(
        "doenca/diagnostico/delete/<uuid:pk>/",
        DiagnosticoDeleteView.as_view(),
        name="diagnostico-delete",
    ),
    path(
        "doenca/diagnostico/restore/<uuid:pk>/",
        DiagnosticoRestoreView.as_view(),
        name="diagnostico-restore",
    ),
]
from django.urls import path, include
from doenca.views.apresentacao import (
    ApresentacaoCreateView,
    ApresentacaoDetailView,
    ApresentacaoDeleteView,
    ApresentacaoListView,
    ApresentacaoRestoreView,
    ApresentacaoUpdateView,
)

# URLs do Models Apresentacao
urlpatterns += [
    path(
        "doenca/apresentacao/", ApresentacaoListView.as_view(), name="apresentacao-list"
    ),
    path(
        "doenca/apresentacao/create/",
        ApresentacaoCreateView.as_view(),
        name="apresentacao-create",
    ),
    path(
        "doenca/apresentacao/<uuid:pk>/",
        ApresentacaoDetailView.as_view(),
        name="apresentacao-detail",
    ),
    path(
        "doenca/apresentacao/update/<uuid:pk>/",
        ApresentacaoUpdateView.as_view(),
        name="apresentacao-update",
    ),
    path(
        "doenca/apresentacao/delete/<uuid:pk>/",
        ApresentacaoDeleteView.as_view(),
        name="apresentacao-delete",
    ),
    path(
        "doenca/apresentacao/restore/<uuid:pk>/",
        ApresentacaoRestoreView.as_view(),
        name="apresentacao-restore",
    ),
]
