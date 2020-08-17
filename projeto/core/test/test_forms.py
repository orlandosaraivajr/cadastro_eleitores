from django.test import TestCase
from core.forms import EleitorForm, EleitorRedeSocialForm


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


class EleitorRedeSocialFormTest(TestCase):
    def test_form_has_fields(self):
        form = EleitorRedeSocialForm()
        expected = ['facebook_id', 'twitter_id', 'foursquare_id']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_ao_menos_uma_rede_social(self):
        form = self.make_validated_form(facebook_id='',twitter_id='', foursquare_id='')
        errors = form.errors
        errors_list = errors['__all__']
        msg = 'Informe ao menos uma rede social'
        self.assertEqual([msg], errors_list)

    def test_sem_facebook(self):
        '''Permitido não ter facebook, mas ao menos uma rede social '''
        form = self.make_validated_form(facebook_id='')
        self.assertEqual(None, form.cleaned_data['facebook_id'])
        self.assertEqual('orlandosaraivaj', form.cleaned_data['twitter_id'])

    def test_sem_twitter(self):
        '''Permitido não ter twitter, mas ao menos uma rede social '''
        form = self.make_validated_form(twitter_id='')
        self.assertEqual('orlandosaraivajr', form.cleaned_data['facebook_id'])
        self.assertEqual(None, form.cleaned_data['twitter_id'])

    def make_validated_form(self, **kwargs):
        valid = dict(
            facebook_id='orlandosaraivajr',
            twitter_id='orlandosaraivaj',
            foursquare_id='orlandosaraiva'
        )
        data = dict(valid, **kwargs)
        form = EleitorRedeSocialForm(data)
        form.is_valid()
        return form
