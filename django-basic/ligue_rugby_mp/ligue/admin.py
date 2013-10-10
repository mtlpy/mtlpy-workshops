from django.contrib import admin

from ligue.models import Equipe, Joueur

class EquipeAdmin(admin.ModelAdmin):
    pass

class JoueurAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'equipe',]

admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Joueur, JoueurAdmin)
