from . import views
from django.urls import path

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.PostList.as_view())
    # path('', views.index),
]
