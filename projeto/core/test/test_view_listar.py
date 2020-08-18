from core.models import EleitorModel, EleitorRedeSocialModel
from django.shortcuts import resolve_url as r
from django.test import TestCase


class coreGetListar(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:listar'))
        self.resp2 = self.client.get(r('core:listar'), follow=True)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'listar.html')
        self.assertTemplateUsed(self.resp2, 'listar.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
        self.assertEqual(200, self.resp2.status_code)

    def test_html(self):
        tags = (
            ('<html lang="pt-br">', 1),
            ('<body>', 1),
            ('Projeto Exemplo', 1),
            ('Cadastro Eleitores', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class corePostListar(TestCase):
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
            twitter_id='twitter_saraiva',
            foursquare_id='',
        )
        self.eleitor_rede_social.save()
        data = {'eleitor_id': self.eleitor.pk}
        self.resp = self.client.post(r('core:listar'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Projeto Exemplo', 1),
            ('Cadastro Eleitores', 1),
            ('orlandosaraivajr', 1),
            ('twitter_saraiva', 1),
            ('Rio Claro', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class corePostListar_sem_dados(TestCase):
    def setUp(self):
        data = {}
        self.resp = self.client.post(r('core:listar'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Projeto Exemplo', 1),
            ('Cadastro Eleitores', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
