from django.db import models

from core.models import User


class Level(models.Model):
    num = models.IntegerField(unique=True)
    max_points = models.FloatField()


class UserLevelProgress(models.Model):
    user = models.ForeignKey(User, verbose_name='user', related_name='level_progress', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, verbose_name='level', on_delete=models.CASCADE)
    points = models.FloatField(default=0)
