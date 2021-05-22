from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)

class Movie(models.Model):
    genres = models.ManyToManyField(
        Genre,
        related_name='movies'
    )
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=200)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movie')

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)