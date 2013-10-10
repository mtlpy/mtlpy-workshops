from django.shortcuts import render

from ligue.models import Equipe

def home(request):
    equipes = Equipe.objects.all()

    c = { 
        "user":"davin", 
        "equipes":equipes,
    }
    return render(request, 'home.html', c)
