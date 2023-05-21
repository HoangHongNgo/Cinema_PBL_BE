from django.urls import path
from .views import *

urlpatterns = [
    path('show/<int:pk>/', ListTicketView.as_view())
]
