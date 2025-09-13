from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase
class SignInTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='username', password='password', email='unit@test.com')
        self.user.save()
    def tearDown(self):
        self.user.delete()
    def test_correct(self):
        user = authenticate(username='username', password='password')
        self.assertTrue((user is not None) and user.is_authenticated)
    def test_wrong_username(self):
        user = authenticate(username='wrong', password='password')
        self.assertFalse(user is not None and user.is_authenticated)
    def test_wrong_pssword(self):
        user = authenticate(username='username', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
