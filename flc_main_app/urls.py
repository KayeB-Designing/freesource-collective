from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('accounts/login', views.LogIn.as_view(), name="login"),
    path('accounts/register/', views.Register.as_view(), name="register"),
    path('resources/', views.ResourceList.as_view(), name="resource_list"),
    path('resources/new/', views.ResourceCreate.as_view(), name="resource_create"),
    path('resources/<int:pk>/', views.ResourceDetail.as_view(), name="resource_detail"),
    path('resources/<int:pk>/update',views.ResourceUpdate.as_view(), name="resource_update"),
    path('resources/<int:pk>/delete',views.ResourceDelete.as_view(), name="resource_delete"),
]