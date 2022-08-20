from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model


class TestName(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_test = get_user_model().objects.create_user(
            username='user-test-1',
            password="poolooshk",
            email='email-test@yahoo.com',
            age=19
        )

    # test 200
    def test_signup_page(self):
        response = self.client.get(reverse('signup_url'))
        self.assertEqual(response.status_code, 200)

    # test 200
    def test_signup_page_without_reverse(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    # test signup only form (not signup page)
    def test_signup_form(self):
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0], self.user_test)
