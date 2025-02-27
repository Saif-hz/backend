from django.contrib.auth.backends import BaseBackend
from .models import Artist, Producer
from django.contrib.auth.hashers import check_password

class CustomUserBackend(BaseBackend):
    """
    Custom authentication backend that checks both Artists and Producers.
    """

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Artist.objects.get(email=email)
        except Artist.DoesNotExist:
            try:
                user = Producer.objects.get(email=email)
            except Producer.DoesNotExist:
                return None  # No user found

        # 🔥 Check password
        if check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        """
        Used by Django to retrieve the user instance.
        """
        try:
            return Artist.objects.get(pk=user_id)
        except Artist.DoesNotExist:
            try:
                return Producer.objects.get(pk=user_id)
            except Producer.DoesNotExist:
                return None
