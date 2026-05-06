from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва жанру")
    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва гри")
    description = models.TextField(verbose_name="Опис гри")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Посилання на фото")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Platform(models.Model):
    name = models.CharField(max_length=50, verbose_name="Платформа")
    games = models.ManyToManyField(Game, verbose_name="Ігри на платформі")
    def __str__(self):
        return self.name