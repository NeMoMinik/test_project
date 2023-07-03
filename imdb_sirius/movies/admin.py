from django.contrib import admin
from .models import Movie, OriginalName, DirectorMovie, Director, Type


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'originalname')
    list_editable = ('name', )


@admin.register(OriginalName)
class OriginalNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


@admin.register(DirectorMovie)
class DirectorMovieAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'director_id')

