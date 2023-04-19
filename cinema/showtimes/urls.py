from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowView.as_view()),
]
