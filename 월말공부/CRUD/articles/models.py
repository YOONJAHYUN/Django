from django.db import models

# Create your models here.
# 데이터 받을 때 표랑 제목 뼈대?
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)