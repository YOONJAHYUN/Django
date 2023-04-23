from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('actor/', views.actor_list),
    path('actor/<int:actor_pk>/', views.actor_detail),
    path('movie/', views.movie_list),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('review/', views.review_list),
    path('review/<int:review_pk>/', views.review_detail),
    path('movie/<int:movie_pk>/review/', views.create_review),
]