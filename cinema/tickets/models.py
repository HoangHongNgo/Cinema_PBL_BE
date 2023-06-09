from django.db import models
from showtimes.models import Showtime
from users.models import User
from cinemas.models import *
# Create your models here.


class Payment(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="payments", default='')
    sale_time = models.DateTimeField(auto_now_add=True)


class Ticket(models.Model):
    showtime = models.ForeignKey(
        Showtime, on_delete=models.SET_NULL, blank=True, null=True)
    seat_num = models.IntegerField()
    seat_row = models.CharField(max_length=2)
    price = models.IntegerField(default=50)
    payment = models.ForeignKey(
        Payment, on_delete=models.SET_NULL, default=None, blank=True, null=True, related_name="tickets")
