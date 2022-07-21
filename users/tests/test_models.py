from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersModelsTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='user',
                                             slug='user',
                                             password='python2022',
                                             mobile='123456789123',
                                             email='user1@gmail.com'
                                             )

    def test_user_status(self):
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_get_absolute_url(self):
        self.assertEqual('/user/profile/user/', self.user.get_absolute_url())
