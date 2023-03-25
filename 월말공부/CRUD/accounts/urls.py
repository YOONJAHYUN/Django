from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # url 참고하는 경로를 만드는 것.
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('delete/', views.delete, name="delete"),
    path('update/', views.update, name="update"),
    path('password/', views.change_password, name="change_password"),
    
]