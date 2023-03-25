from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles':articles
    }
    
    # request를 articles/index.html에 넘겨준다.
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    
    # POST
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        # 유효성 검사 
        if form.is_valid():
            article = form.save()

            return redirect('articles:detail', article.pk)
    # GET
    else:
        form = ArticleForm()
    # 유효성 검사를 실패하거나 else문 통과시 create page에 있어야함.
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def update(request, pk):
    
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        # update를 하기 위해서는 원래 있던 정보를 instance로 불러온다.
        form = ArticleForm(request.POST, request.FILES, instance=article)
        
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article':article
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    # redirect는 view는 다시 실행시키는 것임.(괄호안에 있는게 views 함수 실행)
    # render는 정보를 보내는 것 (html자체를 걍 실행)
    # 따라서 render를 사용하면 정보가 보내지는 것이니까..
    # redirect를 써야한다.
    return redirect('articles:index')