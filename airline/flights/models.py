from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    duration = models.IntegerField()
    weather = models.CharField(max_length=60)
