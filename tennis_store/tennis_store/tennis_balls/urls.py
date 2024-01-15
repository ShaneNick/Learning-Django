from django.urls import path, include
from . import views

#URL configs
urlpatterns = [
    path('hello/', views.ball_count),
]
