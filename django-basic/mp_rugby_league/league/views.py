# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from league.models import Team, Player

def team_list(request):
    teams = Team.objects.all()
    c = {
        'teams': teams,
    }
    return render(request, "league/team_list.html", c)

def team_detail(request, id):
    team = Team.objects.get(id=id)
    c = {
        'team': team,
    }
    return render(request, "league/team_detail.html", c)

def player_list(request):
    players = Player.objects.all()
    c = {
        'players': players,
    }
    return render(request, "league/player_list.html", c)

@login_required
def player_detail(request, id):
    player = Player.objects.get(id=id)
    c = {
        'player': player,
    }
    return render(request, "league/player_detail.html", c)
