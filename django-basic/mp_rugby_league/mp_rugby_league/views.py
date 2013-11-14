# -*- encoding: utf-8 -*-

from django.shortcuts import render

def home(request):
    """Web site home page"""
    c = {}
    return render(request, 'home.html', c)
