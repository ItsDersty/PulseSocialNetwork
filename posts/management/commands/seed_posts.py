import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django_neural_feed.conf import app_settings  # Adjust path to your library settings
from ...models import Post  # Adjust path to your Post model


class Command(BaseCommand):
    help = "Seeds the database with thousands of dummy posts and random embeddings."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=20000, help="Number of posts to generate"
        )

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.first()

        if not user:
            user = User.objects.create_user(
                username="seed_master", password="password123"
            )

        count = options["count"]
        dimensions = app_settings.VECTOR_DIMENSION

        self.stdout.write(
            f"Starting seed: {count} posts with {dimensions}-dim vectors..."
        )

        posts = []
        for i in range(count):
            # Generate random float vector matching pgvector dimensions
            random_vector = [random.uniform(-1.0, 1.0) for _ in range(dimensions)]

            posts.append(
                Post(
                    author=user,
                    content=f"Fake production post volume {i}. Testing HNSW index performance and post-filtering capabilities.",
                    embedding=random_vector,
                    isReply=False,
                )
            )

        # Bulk insert in chunks to optimize memory usage
        batch_size = 5000
        Post.objects.bulk_create(posts, batch_size=batch_size)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully injected {count} posts directly into the database!"
            )
        )
