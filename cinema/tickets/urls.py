from django.urls import path
from .views import *

urlpatterns = [
    path('show/<int:pk>/', ListTicketView.as_view()),
    path('update/<int:pk>/', TicketUpdatelView.as_view()),
]
