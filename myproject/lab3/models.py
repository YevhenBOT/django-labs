from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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

    def __str__(self):
        return self.title

    # Метод для отримання середнього балу
    def average_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(r.score for r in ratings) / ratings.count(), 1)
        return 0

# Модель для оцінок
class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100, verbose_name="Ваше ім'я")
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Оцінка (1-5)")
    comment = models.TextField(verbose_name="Відгук", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Модель для розсилки
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)