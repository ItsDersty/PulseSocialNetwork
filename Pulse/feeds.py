from django.db.models import Count, F, FloatField, ExpressionWrapper, Value
from django.db.models.functions import Cast, Ln, Extract, Now
from django_neural_feed.feeds import BaseNeuralFeed
from posts.models import Post


class PostFeed(BaseNeuralFeed):
    # 1. Core Feed Identity
    feed_id = "posts_main"
    parent_feed = (
        None  # Optional: Reference to a parent feed class for inheritance hierarchy
    )

    # 2. Target Django Models Configuration
    content_django_model = Post
    interaction_django_model = Post.likes.through

    # 3. Interaction Tracking Pipelines
    mode = (
        "m2m"  # Use "m2m" for ManyToMany fields, or "model" for explicit through models
    )

    # 4. Model & Pipeline Thresholds
    embedding_model_name = (
        "paraphrase-multilingual-MiniLM-L12-v2"  # Overrides global setting
    )
    user_likes_limit = 20  # Max target sample size slice for vector profile aggregation

    # 5. Hybrid Scoring Global Weights (Should ideally sum up to 1.0)
    weight_similarity = 1.0
    weight_freshness = 0.0
    weight_popularity = 0.0

    # 6. Popularity: Logarithmic scaling using natural logarithm to keep viral jumps balanced
    # Ln(Value(1000.0)) scales the metric dynamically, hitting a 1.0 score modifier at 1000 likes.
    popularity_expression = ExpressionWrapper(
        Ln(Cast(Count("likes"), FloatField()) + Value(1.0)) / Ln(Value(1000.0)),
        output_field=FloatField(),
    )

    # 7. Freshness: Time-decay function based on post age in hours
    # Safely subtracts timestamps inside the database, converting the interval to hours.
    freshness_expression = ExpressionWrapper(
        Value(1.0)
        / (Value(1.0) + (Extract(Now() - F("created_at"), "epoch") / 3600.0)),
        output_field=FloatField(),
    )
