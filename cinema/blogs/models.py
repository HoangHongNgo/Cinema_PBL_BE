from django.db import models
from users.models import User
from movies.models import Movie
from cloudinary.models import CloudinaryField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    categories = models.ManyToManyField(
        Category, blank=True)
    movies = models.ManyToManyField(
        Movie, blank=True, null=True,)


class BlogImage(models.Model):
    image = CloudinaryField('image')
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='images', blank=True, null=True,)
