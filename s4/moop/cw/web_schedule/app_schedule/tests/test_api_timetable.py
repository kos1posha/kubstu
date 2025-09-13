from django.test import TestCase
from app_schedule.proxies import ApiTimetable
class ApiTimetableTestCase(TestCase):
    def test_group(self):
        expected = list
        actual = type(ApiTimetable.group(group_code='21-КБ-ПИ1'))
        self.assertEqual(expected, actual)
    def test_teacher(self):
        expected = list
        actual = type(ApiTimetable.teacher(first_name='Владислава', last_name='Мурлина', patronymic='Анатольевна'))
        self.assertEqual(expected, actual)
