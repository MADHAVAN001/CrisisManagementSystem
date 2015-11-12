__author__ = 'shuvamnandi'
from django.test import TestCase
from DontCrysis.models import Subscriber
class SubscriberTestCase(TestCase):
    def setUp(self):
        Subscriber.objects.create(name="Noopur", mobile="83939726", nric="G1322512X", address="NTU Hall 6", age=19, postalcode="637891", email="noopijain@gmail.com")
        Subscriber.objects.create(name="Neethu", mobile="96699184", nric="G1321322S", address="NTU Hall 9", age=20, postalcode="639811", email="neethumohanan@gmail.com")

    def test_correct_data_submission(self):
        sub1=Subscriber.objects.get(name="Noopur")
        sub2=Subscriber.objects.get(name="Neethu")
        self.assertEqual(sub1.email, "noopijain@gmail.com")
        self.assertEqual(sub2.email, "neethumohanan@gmail.com")

