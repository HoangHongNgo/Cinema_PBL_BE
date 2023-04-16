from django.db import models
from casts.models import Cast


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(default=0)
    trailer_id = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.DateField()
    duration_minute = models.PositiveIntegerField()
    age_limit = models.IntegerField()
    cover_image = models.TextField()
    banner_image = models.TextField()
    casts = models.ManyToManyField(
        Cast, related_name='casts', null=True, blank=True)
    director = models.ManyToManyField(
        Cast, related_name='directors', null=True, blank=True)
