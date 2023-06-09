from django.db import models
from movies.models import Movie
from cinemas.models import Cinema, Cinema_Room
# Create your models here.


class Showtime(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.SET_NULL, blank=True, null=True)
    Cinema_Room = models.ForeignKey(
        Cinema_Room, on_delete=models.SET_NULL, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.IntegerField(default=50)
