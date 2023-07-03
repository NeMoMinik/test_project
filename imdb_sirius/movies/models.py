from django.db import models


class OriginalName(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=64)
    originalname = models.OneToOneField(
        OriginalName,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movie'
    )
    type_id = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name='movie'
    )
    director = models.ManyToManyField(
        Director,
        related_name='movie',
    )

    def __str__(self):
        return self.name


class DirectorMovie(models.Model):
    movie_id = models.ForeignKey(
        Movie,
        related_name='directors',
        on_delete=models.DO_NOTHING
    )
    director = models.ForeignKey(
        Director,
        related_name='movies',
        on_delete=models.DO_NOTHING
    )