from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import CommentSerializer, ReviewSerializer
from .models import Comment, Review

# Create your views here.
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, review_pk):
    if request.method == 'GET':
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    if request.method == 'GET':
        serializer = ReviewSerializer(request.user.review_set, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if not request.user.review_set.filter(pk=review_pk):
        return Response({'detail':'권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if not request.user.review_set.filter(pk=review_pk):
        return Response({'detail':'권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'DELETE':
        review.delete()
        return Response({'id':review_pk}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, review_pk, comment_pk):
    if not request.user.review_comments.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response({'id':comment_pk}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user in review.like.all():
        review.like.remove(request.user)
    else:
        review.like.add(request.user)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
