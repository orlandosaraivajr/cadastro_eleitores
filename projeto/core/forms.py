from django import forms
from django.core.exceptions import ValidationError
from core.models import EleitorModel, EleitorRedeSocialModel


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números')
    if len(value) != 11:
        raise ValidationError('CPF deve conter onze números')


class EleitorForm(forms.ModelForm):

    class Meta:
        model = EleitorModel
        fields = ['nome_completo', 'cpf', 'idade', 'naturalidade']

    def clean_nome_completo(self):
        nome = self.cleaned_data['nome_completo']
        palavras = [w.capitalize() for w in nome.split()]
        return ' '.join(palavras)

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        validate_cpf(cpf)
        return cpf

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('nome_completo') and not self.cleaned_data.get('phcpfone'):
            raise ValidationError('Informe seu nome ou cpf')
        return self.cleaned_data


class EleitorRedeSocialForm(forms.ModelForm):

    class Meta:
        model = EleitorRedeSocialModel
        fields = ['facebook_id', 'twitter_id', 'foursquare_id']

    def clean(self):
        self.cleaned_data = super().clean()
        sem_face = not self.cleaned_data.get('facebook_id')
        sem_twitter = not self.cleaned_data.get('twitter_id')
        sem_foursquare = not self.cleaned_data.get('foursquare_id')
        if sem_face and sem_twitter and sem_foursquare:
            raise ValidationError('Informe ao menos uma rede social')
        return self.cleaned_data