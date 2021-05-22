from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:movie_pk>/', views.detail),
    path('<int:movie_pk>/like/', views.like),
]
