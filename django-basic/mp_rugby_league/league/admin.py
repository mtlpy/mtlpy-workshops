from django.contrib import admin

from league.models import Team, Player

class TeamAdmin(admin.ModelAdmin):
    pass

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'firstname', 'team',]

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
