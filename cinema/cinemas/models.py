from django.db import models

# Create your models here.
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)


class Cinema_Chain(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    logo_path = models.TextField()


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=1000)
    cinema_chain = models.ForeignKey(
        Cinema_Chain, null=True, blank=True, on_delete=models.SET_NULL, related_name='cinemas')
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True)


class Cinema_Room(models.Model):
    name = models.CharField(max_length=255)
    cinema = models.ForeignKey(
        Cinema, on_delete=models.SET_NULL, null=True, blank=True)
