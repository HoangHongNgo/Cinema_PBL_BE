from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=115, unique=True)
    description = models.TextField()
