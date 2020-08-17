from django.shortcuts import resolve_url as r
from django.test import TestCase


class coreGetIndex(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('core:index'))
        self.resp2 = self.client.get(r('core:index'), follow=True)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')
        self.assertTemplateUsed(self.resp2, 'index.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
        self.assertEqual(200, self.resp2.status_code)

    def test_html(self):
        tags = (
            ('<html lang="pt-br">', 1),
            ('<body>', 1),
            ('Projeto Exemplo', 1),
            ('Cadastro Eleitores', 1),
            ('<input', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class corePostIndex(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('core:index'))
        self.resp2 = self.client.post(r('core:index'), follow=True)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')
        self.assertTemplateUsed(self.resp2, 'index.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
        self.assertEqual(200, self.resp2.status_code)

    def test_html(self):
        tags = (
            ('<html lang="pt-br">', 1),
            ('<body>', 1),
            ('Projeto Exemplo', 1),
            ('Cadastro Eleitores', 1),
            ('<input', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
