from django.db import models

# Create your models here.
class Music(models.Model):

    singer = models.CharField(max_length=10)
    title = models.TextField()