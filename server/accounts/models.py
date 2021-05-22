from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

class User(AbstractUser):
    pass
