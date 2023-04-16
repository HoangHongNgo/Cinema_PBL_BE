from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieView.as_view()),
    path('trailer/<int:pk>/', views.MovieTrailerView.as_view()),
    path('cover/<int:pk>/', views.MovieCoverView.as_view()),
    path('banner/<int:pk>/', views.MovieBannerView.as_view()),
]
