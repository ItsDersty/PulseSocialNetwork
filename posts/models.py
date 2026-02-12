from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Post(models.Model):
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_posts")


    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"