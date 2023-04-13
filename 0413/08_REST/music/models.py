from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True) # 음악이 등록될때 자동으로 되도록

    def __str__(self):
        return f'{self:title}'