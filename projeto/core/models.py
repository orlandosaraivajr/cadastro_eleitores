from django.db import models
from django.utils import timezone

class EleitorModel(models.Model):
    nome_completo = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=14)
    idade = models.PositiveIntegerField('Idade', default=0, null=True)
    naturalidade = models.CharField('Naturalidade', max_length=200)

    def __str__(self):
        return self.nome_completo