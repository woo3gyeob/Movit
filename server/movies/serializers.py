from rest_framework import serializers
from .models import Movie, Comment, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','content', 'rating')

class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = ('id','genres','title','overview','release_date','vote_average','poster_path','like','comment_set',)

