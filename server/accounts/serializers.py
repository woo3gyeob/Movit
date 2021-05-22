from django.db.models import fields
from django.db.models.fields.related_descriptors import ManyToManyDescriptor
from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.serializers import (
    ReviewSerializer, 
    CommentSerializer,
    )
from movies.serializers import MovieSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # write_only : 시리얼라이징은 하지만 응답에는 포함시키지 않음
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileSerializer(serializers.ModelSerializer):
    review_comment_user = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(
        source='review_comment_user.count', 
        read_only=True
    )
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(
        source='review_set.count', 
        read_only=True
    )
    liked_review = ReviewSerializer(many=True, read_only=True)
    liked_movie = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username','liked_review','liked_movie','review_comment_user','comment_count','review_set','review_count',)