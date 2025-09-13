from django.contrib.auth import get_user_model
from django.test import TestCase
from app_profile.models import Agent
class AgentModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='username', password='password', email='unit@test.com')
        self.agent = Agent.objects.create(user=self.user, group_code='test-group')
    def tearDown(self):
        self.user.delete()
        self.agent.delete()
    def test_str(self):
        expected = f'Agent for {self.user.username}[{self.user.id}]'
        actual = str(self.agent)
        self.assertEqual(expected, actual)
    def test_user_label(self):
        agent = Agent.objects.get(id=1)
        expected = 'Веб-пользователь'
        actual = agent._meta.get_field('user').verbose_name
        self.assertEquals(expected, actual)
    def test_user_help_text(self):
        agent = Agent.objects.get(id=1)
        expected = 'Ссылка на веб-пользователя, представляющего апи-пользователя в данной системе.'
        actual = agent._meta.get_field('user').help_text
        self.assertEquals(expected, actual)
    def test_group_code_label(self):
        agent = Agent.objects.get(id=1)
        expected = 'Группа'
        actual = agent._meta.get_field('group_code').verbose_name
        self.assertEquals(expected, actual)
    def test_group_code_help_text(self):
        agent = Agent.objects.get(id=1)
        expected = 'Номер группы пользователя.'
        actual = agent._meta.get_field('group_code').help_text
        self.assertEquals(expected, actual)
    def test_group_code_length(self):
        agent = Agent.objects.get(id=1)
        expected = 31
        actual = agent._meta.get_field('group_code').max_length
        self.assertEquals(expected, actual)
