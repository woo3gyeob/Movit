from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:movie_pk>/', views.detail),
    path('<int:movie_pk>/like/', views.like),
    path('recommend/', views.MovieRecommend),
    path('action/', views.actionMovieRecommend),
    path('adventure/', views.adventureMovieRecommend),
    path('animation/', views.animationMovieRecommend),
    path('comedy/', views.comedyMovieRecommend),
    path('horror/', views.horrorMovieRecommend),
    path('romance/', views.romanceMovieRecommend),
    path('<int:movie_pk>/comment/create/', views.comment_create),
    path('<int:movie_pk>/comment/delete/<int:comment_pk>/', views.comment_delete),
]
