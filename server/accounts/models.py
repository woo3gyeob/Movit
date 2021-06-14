from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    profileImg = models.ImageField(upload_to="image", blank=True)
    pass
