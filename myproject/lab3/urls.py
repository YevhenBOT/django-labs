from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
]