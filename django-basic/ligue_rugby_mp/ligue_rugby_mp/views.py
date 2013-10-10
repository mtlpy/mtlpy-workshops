# -*- encoding: utf-8 -*-

from django.shortcuts import render

def home(request):
    """Page d'accueil du site"""
    c = {
    }
    return render(request, "home.html", c)
