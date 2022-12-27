from django.db import models
from user.models import SoftDeleteModel 
from django.contrib.auth.models import User
# Create your models here.

class Cartype (models.Model):
    name = models.CharField(max_length=255)

class Bus (models.Model):
    cartype = models.ForeignKey(Cartype, on_delete = models.CASCADE)
    schedule = models.CharField(max_length=255)

class Seat (models.Model):
    bus = models.ForeignKey(Bus, on_delete = models.CASCADE)
    on_reserve = models.BooleanField(default=False)
    saled = models.BooleanField(default=False)

class Ticket (models.Model):
    bus = models.ForeignKey(Bus, on_delete = models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete = models.CASCADE)

class Owner (SoftDeleteModel):
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)