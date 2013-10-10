# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ligue.models import Equipe, Joueur

def equipe_list(request):
    equipes = Equipe.objects.all()
    c = {
        'equipes': equipes,
    }
    return render(request, "ligue/equipe_list.html", c)

def equipe_detail(request, id):
    equipe = Equipe.objects.get(id=id)
    c = {
        'equipe': equipe,
    }
    return render(request, "ligue/equipe_detail.html", c)

def joueur_list(request):
    joueurs = Joueur.objects.all()
    c = {
        'joueurs': joueurs,
    }
    return render(request, "ligue/joueur_list.html", c)

@login_required
def joueur_detail(request, id):
    joueur = Joueur.objects.get(id=id)
    c = {
        'joueur': joueur,
    }
    return render(request, "ligue/joueur_detail.html", c)
