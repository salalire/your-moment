from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class TestUser(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='pass@123'
        )
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.email, 'user1@example.com')
        self.assertTrue(user.check_password('pass@123'))


class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user1',
            password='pass@123'
        )

    def test_login_backend(self):
        login = self.client.login(username='user1', password='pass@123')
        self.assertTrue(login)

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'user1',
            'password': 'pass@123'
        })
        self.assertEqual(response.status_code, 302)


class HomePageTest(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class DashboardTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='user1',
            password='pass@123'
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_logged_in(self):
        self.client.login(username='user1', password='pass@123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)