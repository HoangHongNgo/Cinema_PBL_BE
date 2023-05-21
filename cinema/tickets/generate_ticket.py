from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ticket
from showtimes.models import Showtime


@receiver(post_save, sender=Showtime)
def create_tickets(sender, instance, created, **kwargs):
    if created:
        seat_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        seat_nums = range(1, 18)
        for row in seat_rows:
            for num in seat_nums:
                Ticket.objects.create(
                    showtime=instance,
                    seat_row=row,
                    seat_num=num,
                    price="10.00")
