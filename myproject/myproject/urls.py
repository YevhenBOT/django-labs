from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lab3/', include('lab3.urls')), # Цей рядок підключає твою лабу
]