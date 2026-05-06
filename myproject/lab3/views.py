from django.shortcuts import render, get_object_or_404
from .models import Game, Genre

def index(request):
    # Отримуємо всі ігри та всі жанри з бази даних
    games = Game.objects.all()
    genres = Genre.objects.all()
    return render(request, 'lab3/index.html', {'games': games, 'genres': genres})

def game_detail(request, pk):
    # Отримуємо конкретну гру за її ID (pk)
    game = get_object_or_404(Game, pk=pk)
    genres = Genre.objects.all() # для меню
    return render(request, 'lab3/game_detail.html', {'game': game, 'genres': genres})