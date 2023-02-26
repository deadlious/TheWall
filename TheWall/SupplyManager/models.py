from django.db import models

# Create your models here.


class TheWall(models.Model):
    profile = models.IntegerField(default=0)
    section = models.IntegerField(default=0)
    initialHeight = models.IntegerField(default=0)
    currentHeight = models.IntegerField(default=0)
    taskID = models.IntegerField(default=0)


class BuildHistory(models.Model):
    profile = models.IntegerField(default=0)
    section = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    ice = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
