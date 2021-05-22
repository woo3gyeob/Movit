from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:review_pk>/', views.detail),
    path('create/', views.create),
    path('update/<int:review_pk>/', views.update),
    path('delete/<int:review_pk>/', views.delete),
    path('<int:review_pk>/comment/create/', views.comment_create),
    path('<int:review_pk>/comment/delete/<int:comment_pk>/', views.comment_delete),
    path('<int:review_pk>/like/', views.like),
]
