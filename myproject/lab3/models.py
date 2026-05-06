from django.db import models


# 1. Таблиця Жанрів
class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")

    def __str__(self):
        return self.name


# 2. Таблиця Ігор (пов'язана з Жанром)
class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва гри")
    description = models.TextField(verbose_name="Опис гри")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Додано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return self.title


# 3. Таблиця Платформ (на чому можна грати)
class Platform(models.Model):
    name = models.CharField(max_length=50, verbose_name="Платформа (PC, PS5, etc.)")
    games = models.ManyToManyField(Game, verbose_name="Ігри на цій платформі")

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
