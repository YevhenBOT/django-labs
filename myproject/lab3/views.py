from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Genre, Review
from .forms import ReviewForm, SubscriptionForm


def index(request):
    games = Game.objects.all()
    genres = Genre.objects.all()

    if request.method == 'POST':
        sub_form = SubscriptionForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('index')
    else:
        sub_form = SubscriptionForm()

    return render(request, 'lab3/index.html', {
        'games': games,
        'genres': genres,
        'sub_form': sub_form
    })


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    genres = Genre.objects.all()
    reviews = game.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.game = game
            new_review.save()
            return redirect('game_detail', pk=game.pk)
    else:
        form = ReviewForm()

    return render(request, 'lab3/game_detail.html', {
        'game': game,
        'genres': genres,
        'form': form,
        'reviews': reviews
    })


def category_detail(request, pk):
    category = get_object_or_404(Genre, pk=pk)
    games = Game.objects.filter(genre=category)
    genres = Genre.objects.all()
    return render(request, 'lab3/category_detail.html', {'category': category, 'games': games, 'genres': genres})