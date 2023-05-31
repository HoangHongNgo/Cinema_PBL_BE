from django.shortcuts import render
from .models import Movie
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .utils import create_movie_graph, visualize
# Create your views here.


class MovieView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieTrailerView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()
    serializer_class = MovieTrailerSerializer


class MovieCoverView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()
    serializer_class = MovieCoverSerializer


class MovieBannerView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()
    serializer_class = MovieBannerSerializer


class MovieDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRdfAPIView(APIView):
    def get(self, request, format=None):
        # Assuming you have a Movie instance

        # Generate the RDF graph
        movie_graph = create_movie_graph()

        visualize(movie_graph)

        return Response()


class MovieSearchView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        # Filter movies based on search query
        queryset = self.queryset.filter(
            models.Q(name__icontains=search_query) |
            models.Q(description__icontains=search_query)
            # Add more fields for searching here
        )
        return queryset
