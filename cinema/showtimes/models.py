from django.db import models
from movies.models import Movie
from cinemas.models import Cinema
# Create your models here.


class Showtime(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.SET_NULL, blank=True, null=True)
    cinema = models.ForeignKey(
        Cinema, on_delete=models.SET_NULL, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
