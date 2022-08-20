from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model


class TestName(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_test = get_user_model().objects.create(
            username='user-test-1',
            password="poolooshk",
            email='email-test@yahoo.com',
            age=19
        )

    # test 200
    def test_home_page(self):
        response = self.client.get(reverse('home_url'))
        self.assertEqual(response.status_code, 200)

    # test 200
    def test_home_page_without_reverse(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # test assertContains "Login" and "Home page"
    def test_home_page_assertContains(self):
        response = self.client.get(reverse('home_url'))
        self.assertContains(response, 'Login') or self.assertContains(response, 'Home page')

    # test template used home
    def test_home_templates_used(self):
        response = self.client.get(reverse('home_url'))
        self.assertTemplateUsed(response, 'pages/home.html')
