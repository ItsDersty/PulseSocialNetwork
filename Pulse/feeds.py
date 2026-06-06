from django_neural_feed.feeds import BaseNeuralFeed
from django.db.models import F
from posts.models import Post


class PostFeed(BaseNeuralFeed):
    feed_id = "posts_main"
    content_django_model = Post
    interaction_django_model = Post.likes.through
    mode = "m2m"
    user_likes_limit = 20
    weight_similarity = 1.0
    weight_freshness = 0.0
    weight_popularity = 0.0
