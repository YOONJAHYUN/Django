from django.shortcuts import render

# Create your views here.
def index(request):
    
    info = {
        'name': '자현',
        'age': 26,
    }



    return render(request, 'myapp/index.html', {'info':info})