from commons.choices import MaturityRating
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic.base import View

from profiles.services import ProfileService


class ProfileListView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, *args, **kwargs):
        profiles = ProfileService.profile_list_by_user(user=request.user)
        return render(request, "profiles/index.html", {"profiles": profiles})


class ProfileCreateView(LoginRequiredMixin, View):
    class InputForm(forms.Form):
        name = forms.CharField()
        maturity_rating = forms.ChoiceField(choices=MaturityRating.choices)
        kid_profile = forms.BooleanField(required=False)

    def get(self, request: HttpRequest, *args, **kwargs):
        form = self.InputForm()

        parental_rating: list[tuple[int, str]] = MaturityRating.choices

        context = {
            "form": form,
            "parental_rating": parental_rating,
        }

        return render(request, "profiles/create.html", context)

    def post(self, request: HttpRequest, *args, **kwargs):
        account = request.user

        form = self.InputForm(data=request.POST or None)

        if not form.is_valid():
            return render(request, "profiles/create.html", {"form": form})

        ProfileService.create(**form.cleaned_data, account=account)

        return redirect("profiles:list")
