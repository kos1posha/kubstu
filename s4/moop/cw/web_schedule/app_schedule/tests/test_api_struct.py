from django.test import TestCase
from app_schedule.proxies import ApiStruct
class ApiStructTestCase(TestCase):
    def test_get_all(self):
        expected = dict
        actual = type(ApiStruct.get_all())
        self.assertEqual(expected, actual)
    def test_get_departments(self):
        expected = list
        actual = type(ApiStruct.get_departments())
        self.assertEqual(expected, actual)
    def test_get_groups(self):
        expected = list
        actual = type(ApiStruct.get_groups())
        self.assertEqual(expected, actual)
    def test_get_group_info(self):
        expected = dict
        actual = type(ApiStruct.get_group_info(group='21-КБ-ПИ1'))
        self.assertEqual(expected, actual)
