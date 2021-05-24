from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import CommentSerializer, MovieSerializer, MovieDetailSerializer
from .models import Movie, Comment
from random import sample

# Create your views here.
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movies = movies[:15]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def MovieRecommend(request):
    if request.user.liked_movie.all():
        genre_cnt = dict()
        movies = request.user.liked_movie.all()
        for movie in movies:
            genres = movie.genres.all()
            for genre in genres:
                genre_cnt[genre.pk] = genre_cnt.get(genre.pk, 0) + 1
        favor_genre = sorted(genre_cnt.items(), key=lambda x : x[1], reverse=True)[0][0]
        movies = list(Movie.objects.filter(genres=favor_genre).all())
    else:
        movies = list(Movie.objects.filter(vote_average__gte=7).all())
    movie = sample(movies,15)
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like.all():
        movie.like.remove(request.user)
    else:
        movie.like.add(request.user)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, movie_pk, comment_pk):
    if not request.user.movie_comments.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response({'id':comment_pk}, status=status.HTTP_204_NO_CONTENT)
