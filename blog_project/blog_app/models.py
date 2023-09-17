from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
    author_id = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)
    update_at = models.DateTimeField(default=timezone.now)
    content_poster = models.ImageField(upload_to='posters/')
    is_draft = models.BooleanField()

    def __str__(self): 
        return self.title
    def save(self, *args, **kwargs):
        # '..' 문자열이 포함된 content 필드를 변경
        self.content = self.content.replace('"..', '"')
        super().save(*args, **kwargs)
