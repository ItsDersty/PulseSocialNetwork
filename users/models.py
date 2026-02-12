from django.contrib.auth.models import AbstractUser
from django.db import models

from django_resized import ResizedImageField

class PulseUser(AbstractUser):
    bio = models.TextField(max_length=200, default='No bio yet')
    pfp = ResizedImageField(upload_to='profile_pictures/', default='/static/defaultPfp.jpg', size=[256,256])
    followers = models.ManyToManyField("PulseUser", related_name="followed")

    def __str__(self):
        return self.username