from django.db.models import Q, QuerySet

from profiles.models import Profile



class ProfileService(object):
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
