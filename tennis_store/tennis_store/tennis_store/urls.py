"""
URL configuration for tennis_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Notice 'include' is added here


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tennis-balls/', include('tennis_balls_app.urls')),
    path('auth/', include('user_acc.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_acc.urls')),  # Redirect root to auth
    path('tennis-balls/', include('tennis_balls_app.urls')),  # Keep your tennis-balls URLs here
    path('auth/', include('user_acc.urls')),  # Keep your authentication URLs here
]
