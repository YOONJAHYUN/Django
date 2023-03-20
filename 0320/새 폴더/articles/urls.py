from django.urls import path
from . import views

urlpatterns = [
    # articles하고 enter하면 index로 바로 매칭
    path('', views.index, name='index'),
]
