def create(request):
    title = request.POST.get('title') 
    content = request.POST.get('content')
    article = Article(__(a)__, __(b)__)
    __(c)__
    return render(request, 'articles/create.html')