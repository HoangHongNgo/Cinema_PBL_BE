from django.urls import path
from .views import *

urlpatterns = [
    path('cities/', CityList.as_view()),
    path('cities/<int:pk>/', CityDetail.as_view()),
    path('cinema/', CinemaList.as_view()),
    path('cinema/<int:pk>/', CinemaDetail.as_view()),
    path('cinema/search/', CinemaByCity.as_view()),
]
