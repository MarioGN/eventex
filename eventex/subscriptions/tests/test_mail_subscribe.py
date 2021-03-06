from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Mario Neto', cpf='12345678901',
                    email='marioneto@email.com', phone='18-12345-6789')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'marioneto@email.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Mario Neto',
            '12345678901',
            'marioneto@email.com',
            '18-12345-6789'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
