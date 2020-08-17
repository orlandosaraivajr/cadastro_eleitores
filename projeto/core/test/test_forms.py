from django.test import TestCase
from core.forms import EleitorForm


class EleitorFormTest(TestCase):
    def test_form_has_fields(self):
        form = EleitorForm()
        expected = ['nome_completo', 'cpf', 'idade', 'naturalidade']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_digito_com_mensagem_erro(self):
        form = self.make_validated_form(cpf='ABCD5678901')
        errors = form.errors
        field = 'cpf'
        errors_list = errors[field]
        msg = 'CPF deve conter apenas números'
        self.assertEqual([msg], errors_list)

    def test_cpf_11_digitos_com_mensagem_erro(self):
        form = self.make_validated_form(cpf='1234')
        errors = form.errors
        errors_list = errors['cpf']
        msg = 'CPF deve conter onze números'
        self.assertEqual([msg], errors_list)

    def test_cpf_11_digitos(self):
        form = self.make_validated_form(cpf='1234')
        self.assertListEqual(['cpf'], list(form.errors))

    def test_idade_negativa(self):
        form = self.make_validated_form(idade=-1)
        self.assertListEqual(['idade'], list(form.errors))

    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome_completo='ORLANDO Saraiva')
        self.assertEqual('Orlando Saraiva', form.cleaned_data['nome_completo'])

    def make_validated_form(self, **kwargs):
        valid = dict(
            nome_completo='Orlando Saraiva Jr',
            cpf='12345678901',
            idade=38,
            naturalidade='Mogi Mirim'
        )
        data = dict(valid, **kwargs)
        form = EleitorForm(data)
        form.is_valid()
        return form
