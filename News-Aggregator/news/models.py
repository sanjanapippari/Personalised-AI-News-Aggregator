from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class ArticleFeedback(models.Model):
    

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    article_url = models.URLField()
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)

class FollowedSource(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    source_id = models.CharField(max_length=100)

# Create your models here.

class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  url = models.TextField()
  source = models.CharField(max_length=100, blank=True, null=True)  # ✅ new
  language = models.CharField(max_length=10, blank=True, null=True) # ✅ new
  
  def __str__(self):
    return self.title