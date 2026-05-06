from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Головна
    path('game/<int:pk>/', views.game_detail, name='game_detail'), # Сторінка гри
]