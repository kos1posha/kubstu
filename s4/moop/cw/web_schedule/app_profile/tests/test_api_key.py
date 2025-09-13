from datetime import date, timedelta
from random import randint
from django.test import TestCase
import variables as VAR
from app_profile.proxies import ApiKey
def api_key():
    return ApiKey.get(VAR.API_MASTER_KEY)
def proxy_key():
    return ApiKey(id=0, user_id=0, key='test', is_master=False, is_active=True, read_access=True, write_access=False, created_date=str(date.today()), expired_date=str(date.today() + timedelta(days=30)))
def random_key():
    return ApiKey.new(hex(randint(0, 999999999)))
class ApiKeyTestCase(TestCase):
    def test_str(self):
        def success():
            expected = '{\n  "id": 0,\n  "user_id": 0,\n  "key": "test",\n  "is_master": false,\n  "is_active": true,\n  "read_access": true,\n  "write_access": false,\n  "created_date": "' + str(date.today()) + '",\n  "expired_date": "' + str(date.today() + timedelta(days=30)) + '"\n}'
            actual = str(test)
            self.assertEqual(expected, actual)
        def key_depricated():
            expected = 'This api key is deprecated. You must update it with ApiKey.get'
            actual = str(test)
            self.assertEqual(expected, actual)
        test = proxy_key()
        success()
        test._actual = False
        key_depricated()
    def test_get(self):
        def success():
            expected = ApiKey
            actual = type(api_key())
            self.assertEqual(expected, actual)
        def key_doesnt_exist():
            expected = 404
            actual = ApiKey.get(hex(randint(0, 999999999)))
            self.assertEqual(expected, actual)
        def wrong_master_key():
            """ can't be implemented """
            self.assertTrue(...)
        success()
        key_doesnt_exist()
        wrong_master_key()
    def test_new(self):
        def success():
            expected = ApiKey
            actual = type(ApiKey.new('dev@ruslansoloviev.ru'))
            self.assertEqual(expected, actual)
        def user_doesnt_exist():
            expected = 500
            actual = random_key()
            self.assertEqual(expected, actual)
        def wrong_master_key():
            """ can't be implemented """
            self.assertTrue(...)
        success()
        user_doesnt_exist()
        wrong_master_key()
    def test_toggle(self):
        def success():
            expected = not test.is_active
            self.assertEqual(ApiKey, type(test.toggle()))
            actual = ApiKey.get(test.key).is_active
            self.assertEqual(expected, actual)
        def key_depricated():
            test._actual = False
            self.assertRaises(ReferenceError, test.toggle)
        def key_doesnt_exists():
            expected = 404
            actual = test.toggle()
            self.assertEqual(expected, actual)
        test = ApiKey.new('dev@ruslansoloviev.ru')
        success()
        key_depricated()
        test = proxy_key()
        key_doesnt_exists()
