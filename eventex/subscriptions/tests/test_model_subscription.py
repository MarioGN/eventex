from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Mario Neto',
            cpf='12345678910',
            email='mario.neto@email.com',
            phone='18-123456789'
        )
        self.obj.save()


    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have an auto created_at att    r"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Mario Neto', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must to be False."""
        self.assertEqual(False, self.obj.paid)

