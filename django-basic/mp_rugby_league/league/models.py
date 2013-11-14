from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255, null=True, default="")
    date_of_birth = models.DateField(null=True, blank=True)
    team = models.ForeignKey(Team, null=True, related_name="players")
    
    def __unicode__(self):
        return "%s %s" % (self.name.upper(), self.firstname)
