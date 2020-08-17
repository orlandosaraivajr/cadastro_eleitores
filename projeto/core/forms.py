from django import forms
from django.core.exceptions import ValidationError

from core.models import EleitorModel


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
