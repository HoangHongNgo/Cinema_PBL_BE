from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    trailer_link = models.URLField()
    rating = models.IntegerField()
    release_date = models.DateField()
    duration_minute = models.PositiveIntegerField()
    age_limit = models.IntegerField()
    cover_image = models.ImageField(upload_to='movie_covers/', default='',blank=True)
