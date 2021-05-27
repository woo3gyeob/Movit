from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Review, Comment

# Register your models here.
admin.site.register(Review)
admin.site.register(Comment)
