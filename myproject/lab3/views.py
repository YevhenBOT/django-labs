from django.shortcuts import render, get_object_or_404
from .models import Game, Genre

def index(request):
    games = Game.objects.all()
    genres = Genre.objects.all()
    return render(request, 'lab3/index.html', {'games': games, 'genres': genres})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    genres = Genre.objects.all()
    return render(request, 'lab3/game_detail.html', {'game': game, 'genres': genres})

def category_detail(request, pk):
    category = get_object_or_404(Genre, pk=pk)
    games = Game.objects.filter(genre=category)
    genres = Genre.objects.all()
    return render(request, 'lab3/category_detail.html', {'category': category, 'games': games, 'genres': genres})