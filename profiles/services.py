from typing import Union

from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from django.db.models import Q, QuerySet

from profiles.models import Profile

User = Union[AbstractBaseUser, AnonymousUser]


class ProfileService(object):
    @staticmethod
    def create(
        *,
        name: str,
        account: User,
        maturity_rating: int,
        kid_profile: bool,
    ) -> Profile:
        profile = Profile.objects.create(
            name=name,
            account=account,
            maturity_rating=maturity_rating,
            kid_profile=kid_profile,
        )
        profile.save()
        return profile

    @staticmethod
    def profile_list_by_user(*, user: User) -> QuerySet[Profile]:
        profiles = ProfileService.profile_list()

        query = Q(account=user)
        profiles = profiles.filter(query)
        return profiles

    @staticmethod
    def profile_list() -> QuerySet[Profile]:
        profiles = Profile.objects.filter(is_active=True)
        return profiles
