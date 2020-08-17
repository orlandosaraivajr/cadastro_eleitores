from core.models import EleitorModel, EleitorRedeSocialModel
from django.test import TestCase


class EleitorModelTest(TestCase):
    def setUp(self):
        self.nome_completo = 'Orlando Saraiva'
        self.cpf = 12345678910
        self.idade = 38
        self.naturalidade = 'Rio Claro'
        self.eleitor = EleitorModel(
            nome_completo=self.nome_completo,
            cpf=self.cpf,
            idade=self.idade,
            naturalidade=self.naturalidade,
        )
        self.eleitor.save()

    def test_created(self):
        self.assertTrue(EleitorModel.objects.exists())

    def test_str_do_objeto(self):
        objeto = EleitorModel.objects.all()[0]
        self.assertEqual(str(objeto), self.nome_completo)

    def test_nome_completo(self):
        nome = self.eleitor.__dict__.get('nome_completo', '')
        self.assertEqual(nome, self.nome_completo)

    def test_cpf(self):
        cpf = self.eleitor.__dict__.get('cpf', '')
        self.assertEqual(cpf, self.cpf)

    def test_idade(self):
        idade = self.eleitor.__dict__.get('idade', '')
        self.assertEqual(idade, self.idade)


class EleitorRedeSocialModelTest(TestCase):
    def setUp(self):
        self.eleitor = EleitorModel(
            nome_completo='Orlando Saraiva',
            cpf=12345678910,
            idade=38,
            naturalidade='Rio Claro',
        )
        self.eleitor.save()
        self.eleitor_rede_social = EleitorRedeSocialModel(
            eleitor=self.eleitor,
            facebook_id='orlandosaraivajr',
            twitter_id='orlandosaraivaj',
            foursquare_id='',
        )
        self.eleitor_rede_social.save()

    def test_created(self):
        self.assertTrue(EleitorRedeSocialModel.objects.exists())

    def test_str_do_objeto(self):
        objeto = EleitorRedeSocialModel.objects.all()[0]
        self.assertEqual(str(objeto), 'Orlando Saraiva => orlandosaraivajr')

    def test_facebook_id(self):
        face = self.eleitor_rede_social.__dict__.get('facebook_id', '')
        self.assertEqual(face, 'orlandosaraivajr')

    def test_twitter_id(self):
        twitter = self.eleitor_rede_social.__dict__.get('twitter_id', '')
        self.assertEqual(twitter, 'orlandosaraivaj')

    def test_foursquare_id(self):
        foursquare = self.eleitor_rede_social.__dict__.get('foursquare_id', '')
        self.assertEqual(foursquare, '')
