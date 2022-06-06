from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('login/', views.LogIn.as_view(), name="login"),
    path('register/', views.Register.as_view(), name="register"),
]