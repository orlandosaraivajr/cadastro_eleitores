from django.db import models


class EleitorModel(models.Model):
    nome_completo = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=14)
    idade = models.PositiveIntegerField('Idade', default=0, null=True)
    naturalidade = models.CharField('Naturalidade', max_length=200)

    def __str__(self):
        return self.nome_completo


class EleitorRedeSocialModel(models.Model):
    eleitor = models.ForeignKey(
        EleitorModel, on_delete=models.CASCADE)
    facebook_id = models.CharField(
        'FaceBook', max_length=255, null=True, blank=True)
    twitter_id = models.CharField(
        'Twitter', max_length=255, null=True, blank=True)
    foursquare_id = models.CharField(
        'FourSquare', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.eleitor.nome_completo + ' => ' + self.facebook_id
