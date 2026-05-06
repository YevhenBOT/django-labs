from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва жанру")
    def __str__(self): return self.name

class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва гри")
    description = models.TextField(verbose_name="Опис гри")
    image_url = models.URLField(max_length=500, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Додано це поле

    def __str__(self): return self.title

    def average_rating(self):
        ratings = self.reviews.all()
        return round(sum(r.score for r in ratings) / ratings.count(), 1) if ratings.exists() else 0

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True) # Додано це поле

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Гра")
    ordered_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.user.username} - {self.game.title}"