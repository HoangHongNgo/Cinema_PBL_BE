from django.db import models

# Create your models here.
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=1000)
