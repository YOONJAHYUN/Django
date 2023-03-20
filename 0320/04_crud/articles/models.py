from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 생성 시간
    created_at = models.DateTimeField(auto_now_add=True)

    # 수정 시간
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'제목 : {self.title}'