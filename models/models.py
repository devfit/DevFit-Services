from django.db import models
from django.contrib.auth.models import User
from datetime import date

class LiftData(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)

class LiftHistory(models.Model):
    lift_data = models.ForeignKey(LiftData)
    one_rep_max = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    week = models.IntegerField(default=0)
    cycle = models.IntegerField(default=0)
            
class LiftSet(models.Model):
    lift_history = models.ForeignKey(LiftHistory)
    set = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)



