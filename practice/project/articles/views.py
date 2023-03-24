from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }

    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    
    # DB 생성시
    if request.mothod == 'POST':
        # 변수 지정
        form = ArticleForm(request.POST)

        # 이게 유효하면
        if form.is_valid():
            article = form.save()
            # 해당 detail page로 이동한다.
            return redirect('articles:detail')

    return render(request, 'articles/create.html')
    