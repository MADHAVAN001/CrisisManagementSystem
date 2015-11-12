__author__ = 'shuvamnandi'
from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import resolve
from DontCrysis.views import *

class ViewURLsTest(TestCase):
    def test_homepage_pass(self):
        expected = homepage
        found = resolve('/')
        self.assertEqual(found.func, expected)

    def test_homepage_map1_pass(self):
        expected = homepage
        found = resolve('/homepage/')
        self.assertEqual(found.func, expected)

    def test_homepage_map2_pass(self):
        expected = homepage_map2
        found = resolve('/homepage/map2')
        self.assertEqual(found.func, expected)

    def test_homepage_invalid_login_pass(self):
        expected = invalid_login
        found = resolve('/invalid/')
        self.assertEqual(found.func, expected)

    def test_homepage_login_pass(self):
        expected = login
        found = resolve('/login/')
        self.assertEqual(found.func, expected)

    def test_invalid_login_pass(self):
        expected = invalid_login
        found = resolve('/invalid/')
        self.assertEqual(found.func, expected)

    def test_loggedin_pass(self):
        expected = loggedin
        found = resolve('/loggedin/')
        self.assertEqual(found.func, expected)

    def test_auth_pass(self):
        expected = auth_view
        found = resolve('/auth/')
        self.assertEqual(found.func, expected)

    def test_logout_pass(self):
        expected = logout
        found = resolve('/logout/')
        self.assertEqual(found.func, expected)

    def test_register_success_pass(self):
        expected = register_success
        found = resolve('/register_success/')
        self.assertEqual(found.func, expected)

    def test_subscribe_pass(self):
        expected = createSubscriber
        found = resolve('/subscribe/')
        self.assertEqual(found.func, expected)

    def test_subscriber_successful_pass(self):
        expected = subscriber_successful
        found = resolve('/subscriber_successful/')
        self.assertEqual(found.func, expected)

    def test_crisis_create_success_pass(self):
        expected = crisis_create
        found = resolve('/crisis/create/')
        self.assertEqual(found.func, expected)

    def test_crisis_status_pass(self):
        expected = status_crisis
        found = resolve('/crisis/status/')
        self.assertEqual(found.func, expected)

    def test_user_addreportreceiver_pass(self):
        expected = addReportReceiver
        found = resolve('/user/addreportreceiver/')
        self.assertEqual(found.func, expected)

    def test_user_reportreceiveradded_pass(self):
        expected = report_reciever_added
        found = resolve('/user/reportreceiveradded/')
        self.assertEqual(found.func, expected)




















