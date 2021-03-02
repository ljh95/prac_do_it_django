from . import views
from django.urls import path

urlpatterns = [
    path('blog/<int:pk>/', views.single_post_page),
    path('', views.index),
]
