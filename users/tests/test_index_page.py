from django.test import TestCase, Client
from django.urls import reverse


class TestPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_page_display(self):
        response = self.client.get(reverse('user:index'))
        self.assertEqual(response.status_code, 200)
        # print(response.__dict__)
        # self.assertEqual(response.templates[0].name, 'home.html')
        self.assertTemplateUsed(response, 'home.html')
        html = response.content.decode('utf-8')
        self.assertInHTML('''<li><a href="/user/login/">Login</a></li>''', html, True)
        self.assertInHTML('''<li><a href="/user/logout/">Logout</a></li>''', html, False)
        self.assertInHTML('''<li><a href="/user/profile/">Profile</a></li>''', html, False)