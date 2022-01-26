from django.urls import path

from profiles.views import ProfileCreateView, ProfileListView

app_name = "profiles"

urlpatterns = [
    path("", ProfileListView.as_view(), name="list"),
    path("create/", ProfileCreateView.as_view(), name="create"),
]
