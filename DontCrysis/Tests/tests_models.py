__author__ = 'shuvamnandi'
from django.test import TestCase
from DontCrysis.models import Subscriber
from DontCrysis.models import Crisis

class CrisisTestCase(TestCase):
    def setUp(self):
        Crisis.objects.create(title="Fire Alert", description="Fire in General Hospital at Boon Lay", postalcode="639810", type=1, severity=2, date="2015-10-10", time="21:07:17", personName="Parth Satija", personPhone="84076753", isActive=True)

    def tearDown(self):
        c=Crisis.objects.get(title="Fire Alert")
        c.delete()

    def test_correct_data_submission(self):
        crisis=Crisis.objects.get(title="Fire Alert")
        self.assertEqual(crisis.postalcode, "639810")

class SubscriberTestCase(TestCase):
    def setUp(self):
        Subscriber.objects.create(name="Shweta", mobile="86731264", nric="G1321234X", address="NTU Hall 10", postalcode="639810", age=20, email="shwetaramamurthy@gmail.com")
        Subscriber.objects.create(name="Divesh", mobile="86542364", nric="G1322123S", address="NTU Hall 10", postalcode="639810", age=19, email="divesh.biyani@gmail.com")

    def tearDown(self):
        s2=Subscriber.objects.get(name="Shweta")
        s3=Subscriber.objects.get(name="Divesh")
        s2.delete()
        s3.delete()

    def test_correct_data_submission(self):
        s2=Subscriber.objects.get(name="Shweta")
        s3=Subscriber.objects.get(name="Divesh")
        self.assertEqual(s2.email, "shwetaramamurthy@gmail.com")
        self.assertEqual(s3.email, "divesh.biyani@gmail.com")