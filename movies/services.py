from django.db.models import Q, QuerySet
from django.shortcuts import get_object_or_404

from movies.models import Movie, Video


class MovieService:
    @staticmethod
    def list_by_profile(*, filter=None) -> QuerySet[Movie]:
        if isinstance(filter, Q):
            movies = MovieService.list()
            return movies.filter(filter)
        return MovieService.list().filter(*filter)

    def list() -> QuerySet[Movie]:
        movies = Movie.objects.filter(is_active=True)
        return movies

    def get(*, primary_key: int) -> Movie:
        try:
            movie = MovieService.list().get(pk=primary_key)
            return movie
        except Movie.DoesNotExist:
            return None


class VideoService:
    NotImplemented
