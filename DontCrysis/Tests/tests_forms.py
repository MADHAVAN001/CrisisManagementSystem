from django.test import TestCase
from DontCrysis.forms import CrisisCreateForm
from DontCrysis.forms import SubscriberForm

class CrisisCreateFormTest(TestCase):
    def test_form_pass(self):
        form_data={'title':'Major Fire', 'description':'A Petrol station is on fire', 'postalcode':'641231', 'type':2, 'severity':3, 'personName':'Shuvam', 'personPhone':'92801234'}
        form = CrisisCreateForm(form_data)
        self.assertTrue(form.is_valid())

    def test_form_fail_missing_attribute_title(self):
        #missing attribute title
        form_data={'description':'A Petrol station is on fire', 'postalcode':'641231', 'type':2, 'severity':3, 'personName':'Shuvam', 'personPhone':'92801234'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_description(self):
        #missing attribute description
        form_data={'title':'Major Fire', 'postalcode':'641231', 'type':2, 'severity':3, 'personName':'Shuvam', 'personPhone':'92801234'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_postalcode(self):
        #missing attribute postalcode
        form_data={'title':'Major Fire', 'description':'A Petrol station is on fire', 'type':2, 'severity':3, 'personName':'Shuvam', 'personPhone':'92801234'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_type(self):
        #missing attribute type
        form_data={'title':'Major Fire', 'description':'A Petrol station is on fire', 'postalcode':'641231', 'severity':3, 'personName':'Shuvam', 'personPhone':'92801234'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_severity(self):
        #missing attribute severity
        form_data={'title':'Major Fire', 'description':'A Petrol station is on fire', 'postalcode':'641231', 'type':2, 'personName':'Shuvam', 'personPhone':'92801234'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_personName(self):
        #missing attribute personName
        form_data={'title':'Major Fire', 'description':'A Petrol station is on fire', 'postalcode':'641231', 'type':2, 'severity':3, 'personPhone':'92801234'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_personPhone(self):
        #missing attribute personPhone
        form_data={'title':'Major Fire', 'description':'A Petrol station is on fire', 'postalcode':'641231', 'type':2, 'severity':3, 'personName':'Shuvam'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_incorrect_data_type_type(self):
        #Incorrect data type for type
        form_data={'title':'Major Fire', 'description':'A Petrol station is on fire', 'postalcode':'641231', 'type':'abc', 'severity':3,
                   'personName':'Shuvam', 'personPhone':'92801234'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_greater_attribute_length_personPhone(self):
        #Attribute length greater than bound for personPhone
        form_data={'title':'Major Fire', 'description':'A Petrol station is on fire', 'postalcode':'641231', 'type':'abc', 'severity':3,
                   'personName':'Shuvam', 'personPhone':'928012234'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_greater_attribute_length_postalcode(self):
        #Attribute length greater than bound for postalcode
        form_data={'title':'Major Fire', 'description':'A Petrol station is on fire', 'postalcode':'1641231', 'type':'abc', 'severity':3,
                   'personName':'Shuvam', 'personPhone':'92801234'}
        form = CrisisCreateForm(form_data)
        self.assertEqual(form.is_valid(), False)

class SubscriberFormTest(TestCase):
    def test_form_pass(self):
        form_data={'name':'Shuvam Nandi', 'mobile':'91213809', 'nric':'K7275634', 'address':'22 Nanyang Avenue, Singapore', 'age':20,
                   'postalcode':'639810', 'email':'shuvamnandi7@gmail.com'}
        form = SubscriberForm(form_data)
        self.assertTrue(form.is_valid())

    def test_form_fail_greater_attribute_length(self):
        #Attribute length greater than bound for postalcode
        form_data={'name':'Shuvam Nandi', 'mobile':'91213809', 'nric':'K7275634', 'address':'22 Nanyang Avenue, Singapore', 'age':20,
                   'postalcode':'6398102', 'email':'shuvamnandi7@gmail.com'}
        form = SubscriberForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_incorrect_data_type(self):
        #Incorrect data type for age
        form_data={'name':'Shuvam Nandi', 'mobile':'91213809', 'nric':'K7275634', 'address':'22 Nanyang Avenue, Singapore', 'age':'20a',
                   'postalcode':'639810', 'email':'shuvamnandi7@gmail.com'}
        form = SubscriberForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_name(self):
        #missing attribute name
        form_data={'mobile':'91213809', 'address':'22 Nanyang Avenue, Singapore', 'age':20,
                   'postalcode':'639810', 'email':'shuvamnandi7@gmail.com'}
        form = SubscriberForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_mobile(self):
        #missing attribute mobile
        form_data={'name':'Shuvam Nandi', 'nric':'K7275634', 'age':20, 'postalcode':'639810',
                   'email':'shuvamnandi7@gmail.com'}
        form = SubscriberForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_nric(self):
        #missing attribute nric
        form_data={'name':'Shuvam Nandi', 'mobile':'91213809', 'address':'22 Nanyang Avenue, Singapore', 'age':20,
                   'postalcode':'639810', 'email':'shuvamnandi7@gmail.com'}
        form = SubscriberForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_address(self):
        #missing attribute address
        form_data={'name':'Shuvam Nandi', 'mobile':'91213809', 'nric':'K7275634', 'age':20, 'postalcode':'639810', 'email':'shuvamnandi7@gmail.com'}
        form = SubscriberForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_age(self):
        #missing attribute age
        form_data={'name':'Shuvam Nandi', 'mobile':'91213809', 'nric':'K7275634', 'address':'22 Nanyang Avenue, Singapore',
                   'postalcode':'639810', 'email':'shuvamnandi7@gmail.com'}
        form = SubscriberForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_postalcode(self):
        #missing attribute postalcode
        form_data={'name':'Shuvam Nandi', 'mobile':'91213809', 'nric':'K7275634', 'address':'22 Nanyang Avenue, Singapore', 'age':20,
                   'email':'shuvamnandi7@gmail.com'}
        form = SubscriberForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_email(self):
        #missing attribute email
        form_data={'name':'Shuvam Nandi', 'mobile':'91213809', 'nric':'K7275634', 'address':'22 Nanyang Avenue, Singapore', 'age':20, 'postalcode':'639810'}
        form = SubscriberForm(form_data)
        self.assertEqual(form.is_valid(), False)









