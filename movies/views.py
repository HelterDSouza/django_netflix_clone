from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from profiles.services import ProfileService

from movies.models import Movie, Video
from movies.services import MovieService

# Create your views here.


class MovieListView(View):
    def get(self, request: HttpRequest, profile_id: str, *args, **kwargs):

        profile = ProfileService.get(uuid=profile_id)

        if profile not in ProfileService.profile_list_by_user(user=request.user):
            return redirect("profiles:list")

        query = Q(
            Q(maturity_rating=profile.maturity_rating),
            Q(kid_profile=profile.kid_profile),
        )
        movies = MovieService.list_by_profile(filter=query).order_by("?")
        showcase = movies.first()
        context = {"movies": movies, "show_case": showcase}
        return render(request, "movies/index.html", context)


class MovieDetailView(View):
    def get(self, request: HttpRequest, movie_pk: int, *args, **kwargs):
        movie = MovieService.get(primary_key=movie_pk)

        if not movie:
            return redirect("profiles:list")

        context = {"movie": movie}

        return render(request, "movies/detail.html", context)


class MovieVideoView(View):
    def get(self, request, video_id: int, *args, **kwargs):
        video = Video.objects.get(pk=video_id)
        if not video:
            return redirect("profiles:list")

        context = {"video": video}
        return render(request, "movies/showMovie.html", context)
