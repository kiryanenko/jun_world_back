from django.db import models

from core.models import User


class Achievement(models.Model):
    class Meta:
        verbose_name = 'achievement'
        verbose_name_plural = 'achievements'

    slug = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User, verbose_name='users')
    points = models.FloatField(default=0)
