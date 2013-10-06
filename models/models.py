from django.db import models
from django.contrib.auth.models import User
from datetime import date
    
class LiftSet(models.Model):
    set = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

class LiftHistory(models.Model):
    one_rep_max = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    week = models.IntegerField(default=0)
    cycle = models.IntegerField(default=0)
    sets = models.ManyToManyField(LiftSet, null=True, blank=True)

class LiftData(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    history = models.ManyToManyField(LiftHistory, null=True, blank=True)