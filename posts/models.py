from django.db import models
from django.conf import settings # Импортируем настройки

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

class PostMedia(models.Model):
    # Связываем медиа с постом
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    # Поле для файла (картинка или видео)
    file = models.FileField(upload_to='posts_media/')
    
    # Можно добавить тип, чтобы отличать фото от видео в шаблоне
    is_video = models.BooleanField(default=False)