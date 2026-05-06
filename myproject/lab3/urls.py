from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('game/<str:page_name>/', views.sub_page, name='sub_page'),
]