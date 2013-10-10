from django.shortcuts import render

from ligue.models import Equipe

def equipe_detail(request, id):
    equipe = Equipe.objects.get(id=id)
    c = {
        'equipe': equipe,
    }
    return render(request, "ligue/equipe_detail.html", c)

