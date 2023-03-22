from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 모든 게시글 정보 조회
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# GET /articles/create/  | 게시글 생성 페이지 조회
# POST /articles/create/ | 게시글 생성을 위해 DB에 저장
def create(request):
    # 사용자가 어떤 method로 요청을 보냈는지에 따라서 조건 분기
    # POST 요청에 대한 처리
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            # POST /articles/create/ -> 게시글 생성 요청에 대한 응답으로
            # 게시글을 생성 하는 것으로 본인의 역할을 마쳤다.
            return redirect('articles:index')
    else:
        # GET 요청에 대한 처리 먼저 한다.
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    # 게시글 하나 조회
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def update(request, article_pk):
    # POST 요청에 대한 처리
    article = Article.objects.get(pk=article_pk)

    if request.method == 'POST':
        # form을 생성할 토대가 되는 instance가 없다? -> 생성
        # 1번 게시글을 사용자가 입력한 data로 수정하려면 
        # 1번 게시글을 토대로 data를 반영해야한다.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # GET 요청에 대한 처리
        # form을 생성 할 떄, 토대가 될 instance를 정의
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/update.html', context)
