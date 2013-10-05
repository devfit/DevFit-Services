from django.db import models
from django.contrib.auth.models import User
from datetime import date

class LiftData(models.Model):
    liftName = models.CharField(max_length=200)
    liftMax = models.IntegerField(default=0)
    userId = models.ForeignKey(User)

class LiftHistory(models.Model):
    liftData = LiftData()
    liftDate = models.DateField.auto_now_add()
    week = models.IntegerField(default=0)
    cycle = models.IntegerField(default=0)

class LiftSet(models.Model):
    rep = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)