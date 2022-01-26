from django.urls import path

from movies.views import MovieDetailView, MovieListView, MovieVideoView

app_name = "movies"

urlpatterns = [
    path("detail/<int:movie_pk>/", MovieDetailView.as_view(), name="detail"),
    path("watch/<int:video_id>", MovieVideoView.as_view(), name="watch"),
    path("browse/<str:profile_id>", MovieListView.as_view(), name="index"),
]
