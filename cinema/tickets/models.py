from django.db import models
from showtimes.models import Showtime
from users.models import User
# Create your models here.


class Ticket(models.Model):
    showtime = models.ForeignKey(
        Showtime, on_delete=models.SET_NULL, blank=True, null=True)
    seat_code = models.CharField(max_length=10)
    sale_date = models.DateTimeField(blank=True, null=True)
    price = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    # owner
    # saler
