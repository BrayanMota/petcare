from django.db import models

from core.models import Base


# Create your models here.
class Doenca(Base):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    sinais_clinicos = models.TextField()
    transmissao = models.TextField()
    tratamentos = models.TextField()

    class Meta:
        verbose_name = "Doença"
        verbose_name_plural = "Doenças"
        fields_display = [
            "nome",
            "descricao",
            "sinais_clinicos",
            "transmissao",
            "tratamentos",
        ]
        icon_model = "fas fa-disease"

    def __str__(self):
        return self.nome


class Apresentacao(Base):
    TEXT = "TEXTO"
    IMAGE = "IMAGEM"
    ITEM_TYPE_CHOICES = [
        (TEXT, "Texto"),
        (IMAGE, "Imagem"),
    ]

    doenca = models.ForeignKey(
        Doenca, on_delete=models.CASCADE, related_name="apresentacao"
    )
    ordem = models.PositiveIntegerField()  # Campo para controlar a ordem dos itens
    tipo_conteudo = models.CharField(max_length=10, choices=ITEM_TYPE_CHOICES)
    conteudo_texto = models.TextField(blank=True, null=True)
    conteudo_imagem = models.ImageField(
        upload_to="disease_images/", blank=True, null=True
    )

    class Meta:
        ordering = ["ordem"]
        verbose_name = "Apresentação"
        verbose_name_plural = "Apresentações"
        fields_display = [
            "doenca",
            "ordem",
            "tipo_conteudo",
            "conteudo_texto",
            "conteudo_imagem",
        ]
        icon_model = "fas fa-list-ol"

    def __str__(self):
        return f"{self.get_tipo_conteudo_display()} - {self.doenca.nome} (Ordem: {self.ordem})"


class Diagnostico(Base):
    doenca = models.ForeignKey(
        Doenca, on_delete=models.CASCADE, related_name="diagnostico"
    )
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    testes = models.TextField()

    class Meta:
        verbose_name = "Diagnóstico"
        verbose_name_plural = "Diagnósticos"
        fields_display = ["doenca", "nome", "descricao", "testes"]
        icon_model = "fas fa-stethoscope"

    def __str__(self):
        return f"{self.nome} - {self.doenca.nome}"
