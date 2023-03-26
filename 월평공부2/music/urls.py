from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, 'music/index.html'),
    path('<int:music_pk>/', views.detail, 'music/detail.html'),
    path('create/', views.create, 'music/create.html'),
    # path('<int:music_pk>/delete/', views.delete, 'music/delete.html'),
    # path('<int:music_pk>/update/', views.update, 'music/update.html'),


]
