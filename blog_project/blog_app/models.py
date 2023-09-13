from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
    author_id = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)

    def __str__(self): 
        return self.title
