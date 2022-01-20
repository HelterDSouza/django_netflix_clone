from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic.base import View

from profiles.services import ProfileService


class ProfileListView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, *args, **kwargs):
        profiles = ProfileService.profile_list_by_user(user=request.user)
        return render(request, "profiles/index.html", {"profiles": profiles})

