from django.db import models
from users.models import User
from movies.models import Movie
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        Category, on_delete=models.SET_NULL, blank=True)
    movies = models.ManyToManyField(
        Movie, on_delete=models.SET_NULL, blank=True)