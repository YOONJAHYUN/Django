from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        print(request.FILES)
        # 유효성 검사 통과해서 if문을 넘어가서 detail 페이지로 넘어간 것.
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        
    else:
        form = ArticleForm()
    # get 요청일때 비어있는 것 보여주면 된다.
    context = {'form':form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
    # GET -> 수정
    else:
        form = ArticleForm(instance=article)

    context = {'form': form}
    return render(request, 'articles/update.html', context)

