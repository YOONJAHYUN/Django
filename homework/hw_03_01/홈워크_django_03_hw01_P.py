# app/models.py
from django.db import models

# table의 schema의 역할
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()

    
