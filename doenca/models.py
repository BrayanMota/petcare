from django.db import models

from core.models import Base


# Create your models here.
class Doenca(Base):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    sintomas = models.TextField()
    causas = models.TextField()
    tratamentos = models.TextField()

    class Meta:
        verbose_name = "Doença"
        verbose_name_plural = "Doenças"
        fields_display = ["nome", "descricao", "sintomas", "causas", "tratamentos"]
        icon_model = "fas fa-disease"

    def __str__(self):
        return self.name


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
