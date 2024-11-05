from django.contrib import admin
from .models import Doenca, Apresentacao


class ApresentacaoInline(admin.TabularInline):
    model = Apresentacao
    extra = 1
    fields = [
        "ordem",
        "topico",
        "tipo_conteudo",
        "conteudo_texto",
        "conteudo_imagem",
    ]


class DoencaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    inlines = [ApresentacaoInline]


admin.site.register(Doenca, DoencaAdmin)
