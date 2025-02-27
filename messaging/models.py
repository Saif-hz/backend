from django.db import models
from django.conf import settings

class Conversation(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
