from django.db import models

# Create your models here.
class boardPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)
    tag = models.CharField(max_length=50)