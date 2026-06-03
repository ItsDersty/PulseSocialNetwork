from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "posts"

    def ready(self):
        from django_neural_feed.signals import register_like_signal
        from .models import Post

        # Automatically updates user preference embeddings when a new Like is created
        register_like_signal(
            like_target=Post.likes.through,
            mode="m2m",  # use 'model' if you have likes model; 'm2m' if Many2Many.
        )


from django.apps import AppConfig
