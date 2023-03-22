from django.urls import path
from . import views

app_name = 'chatting'

urlpatterns = [
    path('', views.index, name='index')
]
