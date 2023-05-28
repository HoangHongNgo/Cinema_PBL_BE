from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieView.as_view()),
    path('<int:pk>/', views.MovieDetailView.as_view()),
    path('trailer/<int:pk>/', views.MovieTrailerView.as_view()),
    path('cover/<int:pk>/', views.MovieCoverView.as_view()),
    path('banner/<int:pk>/', views.MovieBannerView.as_view()),
    path('movie_rdf/', views.MovieRdfAPIView.as_view(), name='movie_rdf'),
]
