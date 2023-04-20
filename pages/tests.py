from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
# creating tests for two pages:
# homepage and signup page


class HomePageTests(SimpleTestCase):

    # test to find out if page exists and returns a HTTP  200 status code
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # test to find out if pages uses the correct url name in the view

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))  # use name of url
        self.assertEqual(response.status_code, 200)

    # test to see if proper template is used
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # test name of url
        # test name of tenplate rendered by url
        self.assertTemplateUsed(response, 'home.html')


class SignUpPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
