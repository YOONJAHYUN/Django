# pages/urls.py

from django.urls import path
from . import views

# 변수명 app_name은 꼭 지켜야 한다.
app_name = 'pages'

urlpatterns = [

    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),

]
