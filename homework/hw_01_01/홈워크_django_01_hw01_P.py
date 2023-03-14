# 같은 위치에 있을 경우

from django.urls import path
from my_app import views

urlpatterns = [
    path('hello/', views.hello)
]
