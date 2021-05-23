from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:movie_pk>/', views.detail),
    path('<int:movie_pk>/like/', views.like),
    path('recommend/', views.MovieRecommend),
    path('<int:movie_pk>/comment/create/', views.comment_create),
    path('<int:movie_pk>/comment/delete/<int:comment_pk>/', views.comment_delete),
]
