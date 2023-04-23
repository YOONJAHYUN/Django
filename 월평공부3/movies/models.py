from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    poster_path = models.TextField()
    # 역참조가 필요한 다대다에 realted_name을 붙여서 활용할 수 있게 한다.
    actors = models.ManyToManyField(Actor, related_name='movies')

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)