from django.db import models

"""
class PulseUser(AbstractUser):
    bio = models.TextField(max_length=200, default='No bio yet')
    pfp = ResizedImageField(upload_to='profile_pictures/', default='/static/defaultPfp.jpg', size=[256,256])  # Укажите путь для сохранения изображений
    followers = models.ManyToManyField("PulseUser", related_name="followed")

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(PulseUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    liked_by = models.ManyToManyField("PulseUser", related_name="liked_posts")


    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')  # Укажите путь для сохранения изображений

    def __str__(self):
        return f"Image for post {self.post.id}"
     """