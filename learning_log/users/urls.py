"""为应用程序users定义URL模式"""
from django.urls import path
from django.contrib.auth.views import LoginView
from .import views
urlpatterns = [
    # 用户登录
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注销
    path('logout/', views.logout_view, name='logout'),
    # 注册
    path('register/', views.register, name='register'),
]
