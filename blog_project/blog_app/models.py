from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    author = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)
    tag = models.CharField(max_length=50)

    def __str__(self): 
        return self.title
