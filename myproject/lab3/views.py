from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Game, Genre, Order, Review
from .forms import ReviewForm

def index(request):
    games = Game.objects.all()
    genres = Genre.objects.all()
    return render(request, 'lab3/index.html', {'games': games, 'genres': genres})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    genres = Genre.objects.all()
    form = ReviewForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.game = game
        review.save()
        return redirect('game_detail', pk=game.pk)
    return render(request, 'lab3/game_detail.html', {'game': game, 'genres': genres, 'form': form, 'reviews': game.reviews.all()})

@login_required
def buy_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    Order.objects.create(user=request.user, game=game)
    return render(request, 'lab3/order_success.html', {'game': game})

@login_required
def profile(request):
    genres = Genre.objects.all()
    orders = Order.objects.all() if request.user.is_superuser else Order.objects.filter(user=request.user)
    return render(request, 'lab3/profile.html', {'orders': orders, 'genres': genres})

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')
    return render(request, 'lab3/register.html', {'form': form, 'genres': Genre.objects.all()})

def logout_view(request):
    logout(request)
    return redirect('index')

def category_detail(request, pk):
    category = get_object_or_404(Genre, pk=pk)
    return render(request, 'lab3/category_detail.html', {'category': category, 'games': Game.objects.filter(genre=category), 'genres': Genre.objects.all()})