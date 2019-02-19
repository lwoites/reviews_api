from rest_framework.authtoken.models import Token
from django.test import TestCase
from consumeraffairs.users.models import Reviewer
import consumeraffairs.users.signals

class UserModelTests(TestCase):

    def test_token_created_for_new_user(self):
        user = Reviewer(username="user__1")
        user.set_password('user_1')
        user.save()

        self.assertEqual(Token.objects.last().user, user)
