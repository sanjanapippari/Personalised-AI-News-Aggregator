from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
class UserFeedback(models.Model):
    FEEDBACK_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_url = models.URLField()
    article_title = models.CharField(max_length=300)
    image = models.URLField(blank=True, null=True)     # ✅ Add this
    source = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this
    action = models.CharField(max_length=10, choices=FEEDBACK_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.article_title[:40]}"
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
   location = models.CharField(max_length=100, null=True, blank=True)

