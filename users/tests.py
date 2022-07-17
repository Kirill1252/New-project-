from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.all().delete()

    def test_create_user(self):
        User = get_user_model()
        self.assertEqual(User.objects.count(), 0)
        self.user1 = User.objects.create_user(username='User1',
                                              slug='User1',
                                              password='python2022',
                                              mobile='123456789123',
                                              email='user1@gmail.com'
                                              )
        self.user2 = User.objects.create_user(username='User2',
                                              slug='User2',
                                              password='python2022',
                                              mobile='380335478944',
                                              email='user2@gmail.com'
                                              )
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(self.user1.username, 'User1')
        self.assertEqual(self.user1.mobile, '123456789123')
        self.assertEqual(self.user1.email, 'user1@gmail.com')
        self.assertEqual(self.user1.slug, 'User1')

        self.assertTrue(self.user1.is_active)
        self.assertFalse(self.user1.is_staff)
        self.assertFalse(self.user1.is_superuser)

        self.assertEqual(self.user2.username, 'User2')
        self.assertEqual(self.user2.mobile, '380335478944')
        self.assertEqual(self.user2.email, 'user2@gmail.com')
        self.assertEqual(self.user2.slug, 'User2')

        self.assertTrue(self.user2.is_active)
        self.assertFalse(self.user2.is_staff)
        self.assertFalse(self.user2.is_superuser)
