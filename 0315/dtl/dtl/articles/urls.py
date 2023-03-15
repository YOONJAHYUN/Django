# articles/urls.py

from django.urls import path
from . import views

# 변수명 app_name은 꼭 지켜야 한다.
app_name = 'articles'

urlpatterns = [
    # URL mapping -> include
    # Naming URL patterns
    path('index/', views.index, name='index'), # 이 이름으로 불러온다.
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),

    # 문자열 말고 숫자로 받고싶을때..
    path('<int:age>/', views.info, name='age'),
    # insta 주소창 마냥..
    path('<name>/', views.profile, name='porfile'),
]
