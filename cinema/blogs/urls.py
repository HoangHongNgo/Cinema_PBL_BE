from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view()),
    path('post', views.BlogAddView.as_view()),
]
