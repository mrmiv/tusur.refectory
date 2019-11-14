from django.test import TestCase
from django.contrib import auth
from .models import ExtUser as User

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('test@dom.com', 'pass')
        self.u.is_admin = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(email='test@dom.com', password='pass')
