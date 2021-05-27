from django.contrib import admin
from .models import Movie, Genre, Comment
# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Comment)