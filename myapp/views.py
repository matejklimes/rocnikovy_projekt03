from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import GameForm
from .models import Game, Developer


def index(request):
    games = Game.objects.all()
    developers = Developer.objects.all()

    context = {
        'games': games,
        'developers': developers,
    }

    return render(request, 'index.html', context)


class DeveloperListView(ListView):
    model = Developer
    context_object_name = 'developers'
    template_name = 'developer/developer_list.html'


class DeveloperDetailView(DetailView):
    model = Developer
    context_object_name = 'developer'
    template_name = 'developer/developer_detail.html'


class GameListView(ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'game/game_list.html'


class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'game/game_detail.html'


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'game/games_form.html'
    success_url = reverse_lazy('games_list')
