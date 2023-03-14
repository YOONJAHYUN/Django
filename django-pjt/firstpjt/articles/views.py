from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # app_name/templates/app_name/
    # articles/templates/articles
    context = {
        'num':30
    }
    return render(request, 'articles/index.html', context)
