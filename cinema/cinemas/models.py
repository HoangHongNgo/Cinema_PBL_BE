from django.db import models

# Create your models here.
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=1000)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True)


class Cinema_Room(models.Model):
    name = models.CharField(max_length=255)
    cinema = models.ForeignKey(
        Cinema, on_delete=models.SET_NULL, null=True, blank=True)
