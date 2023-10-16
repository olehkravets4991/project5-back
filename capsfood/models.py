from django.db import models

# Create your models here.
class Capsfood(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)