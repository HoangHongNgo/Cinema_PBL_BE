from django.db import models

# Create your models here.


class Cast(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_path = models.TextField()
    date_of_birth = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=255)
