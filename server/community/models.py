from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_review')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_comments')
    created_at = models.DateTimeField(auto_now_add=True)