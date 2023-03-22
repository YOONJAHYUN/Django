from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }

    return render(request, 'articles/index.html', context)


# def create(request):

#     form = ArticleForm()
#     return 