from core.models import EleitorModel, EleitorRedeSocialModel
from django.shortcuts import resolve_url as r
from django.test import TestCase


class coreGetCadastro(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:cadastro'))
        self.resp2 = self.client.get(r('core:cadastro'), follow=True)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')
        self.assertTemplateUsed(self.resp2, 'cadastro.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
        self.assertEqual(200, self.resp2.status_code)

    def test_html(self):
        tags = (
            ('<html lang="pt-br">', 1),
            ('<body>', 1),
            ('Projeto Exemplo', 1),
            ('Cadastro Eleitores', 1),
            ('Dados Eleitor', 1),
            ('Rede Social', 1),
            ('<input', 9),
            ('<br>', 13),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class corePostCadastroOk(TestCase):
    """Neste teste, os dados estão corretos."""
    def setUp(self):
        data = {'nome_completo': 'orlando saraiva',
                'cpf': '12345678910',
                'idade': 38,
                'naturalidade': 'rio claro',
                'facebook_id': 'orlandosaraivajr',
                'twitter_id': 'orlandosaraivaj'}
        self.resp = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_dados_persistidos(self):
        self.assertTrue(EleitorModel.objects.exists())
        self.assertTrue(EleitorRedeSocialModel.objects.exists())

    def test_dados_eleitores_sem_formatacao(self):
        eleitor = EleitorModel.objects.all()[0]
        self.assertEqual(eleitor.cpf, '12345678910')
        self.assertEqual(eleitor.idade, 38)

    def test_dados_eleitores_formatados(self):
        eleitor = EleitorModel.objects.all()[0]
        self.assertEqual(eleitor.nome_completo, 'Orlando Saraiva')
        self.assertEqual(eleitor.naturalidade, 'Rio Claro')

    def test_dados_redes_sociais_sem_formatacao(self):
        eleitor_rede_sociais = EleitorRedeSocialModel.objects.all()[0]
        self.assertEqual(eleitor_rede_sociais.facebook_id, 'orlandosaraivajr')
        self.assertEqual(eleitor_rede_sociais.twitter_id, 'orlandosaraivaj')
        self.assertEqual(eleitor_rede_sociais.foursquare_id, None)


class corePostCadastroFail_1(TestCase):
    """Nenhum dado é enviado via post. """
    def setUp(self):
        data = {}
        self.resp = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Informe o nome completo', 1),
            ('Informe um CPF válido', 1),
            ('Informe a naturalidade', 1),
            ('Informe ao menos uma rede social', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class corePostCadastroFail_2(TestCase):
    """Neste teste, apenas o CPF é informado, e menos que onze números"""
    def setUp(self):
        data = {'cpf': '123'}
        self.resp = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Informe o nome completo', 1),
            ('CPF deve conter onze números', 1),
            ('Informe a naturalidade', 1),
            ('Informe ao menos uma rede social', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class corePostCadastroFail_3(TestCase):
    """Neste teste, apenas o CPF é informado,
    menos que onze números e letras"""
    def setUp(self):
        data = {'cpf': '123A'}
        self.resp = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Informe o nome completo', 1),
            ('CPF deve conter apenas números', 1),
            ('Informe a naturalidade', 1),
            ('Informe ao menos uma rede social', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
