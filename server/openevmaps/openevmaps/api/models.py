from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.
class EVPoint(models.Model):
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    tempature =  models.IntegerField()
    speed = models.DecimalField(max_digits=15,decimal_places=8)
    energy_usage = models.DecimalField(max_digits=10,decimal_places=3)
    #user = models.OneToOneField(settings.AUTH_USER_MODEL)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='evpoint', on_delete=models.CASCADE)

    def __str__(self):
        return ("%d:%d @ %d"%(self.longitude,self.latitude, self.speed))


class EVTrip(models.Model):
    date = models.IntegerField()
    time_start = models.IntegerField()
    time_end = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='evtrip', on_delete=models.CASCADE)
