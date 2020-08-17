from core.models import EleitorModel
from datetime import datetime
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
