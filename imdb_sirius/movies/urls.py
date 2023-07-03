from django.contrib import admin
from django.urls import path, include
from movie_dash.dash import movies_diagram
from .views import get_movies, get_diagram


urlpatterns = [
    path('', get_movies),
    path('diagram/', get_diagram),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]