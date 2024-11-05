from django.db import models

from core.models import Base
from core.utils import save_file_to
from core.validators import FileMaxSizeValidator


# Create your models here.
class Doenca(Base):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(
        "Imagem",
        upload_to=save_file_to,
        blank=True,
        null=True,
        validators=[FileMaxSizeValidator()],
    )

    class Meta:
        verbose_name = "Doença"
        verbose_name_plural = "Doenças"
        fields_display = [
            "nome",
            "descricao",
        ]
        icon_model = "fas fa-disease"

    def __str__(self):
        return self.nome


class Apresentacao(Base):
    TEXT = "TEXTO"
    IMAGE = "IMAGEM"
    TIPO_CONTEUDO = [
        (TEXT, "Texto"),
        (IMAGE, "Imagem"),
    ]

    TOPICO = [
        ("Sinal Clínico", "Sinal Clínico"),
        ("Diagnostico", "Diagnostico"),
        ("Prevenção", "Prevenção"),
        ("Ciclo da Doença", "Ciclo da Doença"),
        ("Boletim Epidemiológico", "Boletim Epidemiológico")
    ]

    doenca = models.ForeignKey(
        Doenca, on_delete=models.CASCADE, related_name="apresentacao"
    )
    topico = models.CharField(verbose_name='Tópico', max_length=30, choices=TOPICO)
    ordem = models.PositiveIntegerField() # Campo para controlar a ordem dos itens
    tipo_conteudo = models.CharField(verbose_name='Tipo', max_length=10, choices=TIPO_CONTEUDO)
    conteudo_texto = models.TextField(verbose_name='Conteúdo do Texto', blank=True, null=True)
    conteudo_imagem = models.ImageField(verbose_name='Conteúdo da Imagem',
        upload_to="disease_images/", blank=True, null=True
    )

    class Meta:
        ordering = ["ordem"]
        verbose_name = "Apresentação"
        verbose_name_plural = "Apresentações"
        fields_display = [
            "doenca",
            "topico",
            "ordem",
            "tipo_conteudo",
            "conteudo_texto",
            "conteudo_imagem",
        ]
        icon_model = "fas fa-list-ol"

    def __str__(self):
        return f"{self.doenca.nome} - {self.topico} - {self.tipo_conteudo} (Ordem: {self.ordem})"


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
