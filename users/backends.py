from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class UsernameOrGmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username:
            try:
                if username.endswith('@gmail.com'):
                    user = User.objects.get(email=username)
                else:
                    user = User.objects.get(username=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None
        return None