from random import randint
from django.test import TestCase
from app_profile.proxies import ApiUser
def api_user():
    return ApiUser.get('dev@ruslansoloviev.ru')
def proxy_user():
    return ApiUser(id=0, first_name='fname', last_name='lname', email='unit@test.com', is_staff=False, is_active=True)
def random_user():
    return ApiUser.new(hex(randint(0, 9999)), hex(randint(0, 9999)), hex(randint(0, 999999999)))
class ApiUserTestCase(TestCase):
    def test_str(self):
        def success():
            test._actual = True
            expected = '{\n  "id": 0,\n  "first_name": "fname",\n  "last_name": "lname",\n  "email": "unit@test.com",\n  "is_staff": false,\n  "is_active": true\n}'
            actual = str(test)
            self.assertEqual(expected, actual)
        def user_depricated():
            test._actual = False
            expected = 'This api user is deprecated. You must update it with ApiUser.get'
            actual = str(test)
            self.assertEqual(expected, actual)
            self.assertRaises(ReferenceError, test.toggle)

        test = proxy_user()
        success()
        user_depricated()
    def test_get(self):
        def success():
            expected = ApiUser
            actual = type(api_user())
            self.assertEqual(expected, actual)
        def user_doesnt_exist():
            expected = 404
            actual = ApiUser.get(hex(randint(0, 999999999)))
            self.assertEqual(expected, actual)
        def wrong_master_key():
            """ can't be implemented """
            self.assertTrue(...)
        success()
        user_doesnt_exist()
        wrong_master_key()
    def test_new(self):
        def success():
            expected = ApiUser
            actual = type(random_user())
            self.assertEqual(expected, actual)
        def sql_constraints_error():
            expected = 400
            actual = ApiUser.new('Ruslan', 'Soloviev', 'dev@ruslansoloviev.ru')
            self.assertEqual(expected, actual)
        def wrong_master_key():
            """ can't be implemented """
            self.assertTrue(...)
        success()
        sql_constraints_error()
        wrong_master_key()
    def test_toggle(self):
        def success():
            expected = not test.is_active
            self.assertEqual(ApiUser, type(test.toggle()))
            actual = ApiUser.get(test.email).is_active
            self.assertEqual(expected, actual)
        def key_depricated():
            test._actual = False
            self.assertRaises(ReferenceError, test.toggle)
        def key_doesnt_exists():
            expected = 404
            actual = test.toggle()
            self.assertEqual(expected, actual)
        test = random_user()
        success()
        key_depricated()
        test = proxy_user()
        key_doesnt_exists()
    def test_keys(self):
        def success():
            expected = list
            actual = type(api_user().keys())
            self.assertEqual(expected, actual)
        def user_or_keys_doesnt_exists():
            expected = 0
            actual = len(random_user().keys())
            self.assertEqual(expected, actual)
        success()
        user_or_keys_doesnt_exists()
    def test_edit(self):
        def success():
            expected = ('fname', 'lname', True)
            api_user = test.edit('fname', 'lname', True)
            actual = (api_user.first_name, api_user.last_name, api_user.is_staff)
            self.assertEqual(expected, actual)
            self.assertEqual(ApiUser, type(api_user))
        def user_depricated():
            test._actual = False
            self.assertRaises(ReferenceError, test.toggle)
        def user_doesnt_exist():
            expected = 404
            actual = test.edit('fname', 'lname', True)
            self.assertEqual(expected, actual)
        test = random_user()
        success()
        user_depricated()
        test = proxy_user()
        user_doesnt_exist()
