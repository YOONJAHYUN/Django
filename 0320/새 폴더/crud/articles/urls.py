from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # ~ / articles / * 로 작성 했을 때
    # * 자리에 오는건 index와 매칭이 된다.
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
