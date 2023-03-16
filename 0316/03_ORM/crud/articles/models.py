from django.db import models

# Create your models here.
class Article(models.Model):
    # max_length 필수 인자
    title = models.CharField(max_length=100)
    content = models.TextField()
