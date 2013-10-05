from django.db import models
from django.contrib.auth.models import User

class LiftData(models.Model):
    liftName = models.CharField(max_length=200)
    liftMax = models.IntegerField(default=0)
    userId = models.ForeignKey(User)