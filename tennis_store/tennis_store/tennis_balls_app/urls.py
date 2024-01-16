from django.urls import path, include
from . import views

#URL configs
urlpatterns = [
    path("", views.home, name= 'home'),
]

