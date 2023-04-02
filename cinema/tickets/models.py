from django.db import models
from showtimes.models import Showtime
# Create your models here.


class Ticket(models.Model):
    showtime = models.ForeignKey(
        Showtime, on_delete=models.SET_NULL, blank=True, null=True)
    seat_code = models.CharField(max_length=10)
    sale_date = models.DateTimeField(blank=True, null=True)
    # owner
    # saler
