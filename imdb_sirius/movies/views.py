from django.shortcuts import render
from .models import Movie, Director


def get_movies(request):
    movies_list = Movie.objects.all().values('name', 'type_id__name', 'director__name')

    context = {
        'movies': movies_list
    }

    template = 'movies/movies_list.html'
    return render(request, template, context)

def get_diagram(request):
    template = 'movies/movies_diagram.html'
    return render(request, template)