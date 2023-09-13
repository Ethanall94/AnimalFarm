from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter
from .views import PostViewset
# from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'posts', PostViewset)

urlpatterns = [
    path('', views.board_client, name='board-client'), # 메인 페이지
    path('write/', views.write, name='write'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('board_admin/',views.board_admin, name='board_admin'),
    path('board/',views.board, name='board'),
    path('board/<str:topic>/', views.board, name='board-topic'),
    path('api/', include(router.urls)),
]