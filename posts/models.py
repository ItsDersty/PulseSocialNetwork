from django.db import models
from django.conf import settings
from django_neural_feed.mixins import NeuralRecommendMixin, NeuralHnswMixin


class Post(NeuralRecommendMixin, models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likedPosts")
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="replies", on_delete=models.SET_NULL
    )
    isReply = models.BooleanField(default=False)

    def get_ready_text(self):
        return f"{self.content}"

    # Explicitly inherit Meta options from the HNSW mixin
    class Meta(NeuralRecommendMixin.Meta, NeuralHnswMixin.Meta):
        pass


class PostMedia(models.Model):
    post = models.ForeignKey(Post, related_name="media", on_delete=models.CASCADE)
    file = models.FileField(upload_to="posts_media/")

    is_video = models.BooleanField(default=False)
