from django.urls import path
from . import views

# 반드시 app_name 해야함!!! 다른거 하지마셈!!
app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
