from django.db import models
from django.contrib.auth.models import User

class LiftData(models.Model):
    name = models.CharField(max_length=200)
    one_rep_max = models.IntegerField(default=0)
    user = models.ForeignKey(User)