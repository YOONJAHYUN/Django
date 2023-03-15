from django.shortcuts import render

# Create your views here.
def index(request):
    # rendering 하는 이유 : 상속과 변수,, 등 반복..이런것들을 html로 만들어서 사용자에게 넘겨주는 느낌쓰..
    return render(request, 'articles/index.html')

def create(request):
    return render(request, 'articles/create.html')

def profile(request, name):
    # context 이름은 관념적인것..
    context = {
        'name':name
    }
    return render(request, 'articles/profile.html', context)

def info(request, age):
    context = {
        'age':age
    }
    return render(request, 'articles/info.html', context)