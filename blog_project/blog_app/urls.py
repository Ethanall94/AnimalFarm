from django.urls import path, include
from django.contrib import admin
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.board_cilent, name='board-cilent'), # 메인 페이지
    path('write', views.write, name='write'),
    path('login', views.login, name='login'),
    path('board_admin',views.board_admin, name='board_admin'),
    path('board',views.board, name='board')
]